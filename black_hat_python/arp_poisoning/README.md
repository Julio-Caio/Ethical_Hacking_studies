## Pré-requisitos

- Python 3.x
- Scapy

### Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalação

```bash
pip3 install scapy
```

## Executando o código

```bash
sudo python3 arper.py -i <interface> -t <target_ip> -g <gateway_ip>
```

### Output 

O script irá salvar os pacotes ARP em um arquivo chamado `arp_poisoning.pcap` na mesma pasta onde o script está localizado. Você pode usar o Wireshark para abrir e analisar esse arquivo.