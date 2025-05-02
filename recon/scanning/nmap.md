<h1>Curiosidades sobre o Nmap</h1>

<h3>Identificando o sistema operacional</h3>

```
nmap -O <target_IP>
```

O nmap -O (opção de OS detection) tenta identificar o sistema operacional subjacente, e isso geralmente significa detectar o kernel, especialmente no caso de sistemas baseados em Unix/Linux.

Ele não tem como foco detectar a distribuição (como Ubuntu, Debian, Fedora, etc.), porque isso exige informações mais específicas que geralmente não são acessíveis via varredura de rede padrão.

A detecção se baseia em características do TCP/IP stack (como o tamanho da janela TCP, TTL, opções IP/TCP, etc.), que são controladas pelo kernel — e não por softwares de espaço do usuário (como a GUI ou o sistema de pacotes da distro).

<h3>UDP Scanning</h3>

```
nmap -sU <target_IP>
```

O UDP scanning no Nmap funciona enviando pacotes UDP para as portas-alvo.

- UDP não possui handshake como o TCP — não há SYN/ACK, nem confirmação de entrega. Isso dificulta a detecção precisa do estado da porta.

- Quando **nenhuma resposta** é recebida, o Nmap marca a porta como **open|filtered**, pois ela pode estar aberta (mas o serviço não respondeu) ou pode estar sendo filtrada por um firewall.

- Quando o Nmap recebe uma mensagem ICMP do tipo 3, código 3 (**"Destination Port Unreachable"**), ele conclui que a porta está **closed**.

<h3>Nmap scripting</h3>

- O Nmap possui diversas funcionalidades, uma delas são seus scripts, estes que são organizados em categorias: auth, broadcast, brute, default, discovery...

- Exemplo: Se você quiser rodar a funcionalidade que possui todos os scripts de discovery, é só rodar:

```
    nmap -sS --script=discovery <target_IP>
```

- Normalmente, em sistema Unix/Linux, o diretório padrão onde os scripts do nmap estarão inclusos é o **/usr/share/nmap/scripts**

- Caso possua dúvida na utilização de um script, é só digitar o comando:

```
nmap --script -help=<nome_do_script>.nse
```

Os scripts nmap possuem a extensão **.nse**, ou seja, ***Nmap Scripting Engine***, além de que são construídos na linguagem ***Lua***.