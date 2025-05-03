## Nmap

**nmap -sS**
- Envia um pacote SYN, e após o host alvo responder com SYN/ACK, o nmap envia um pacote RST para finalizar a conexão;

**nmap -sT**
- Faz o fluxo completo do TCP (SYN -> SYN/ACK -> ACK)

**nmap -sF**
- Envia um pacote FYN, se a porta estiver fechada ela enviará um pacote RST
- Se estiver aberta, não irá responder 

---

| Tipo de Varredura        | Comando | Funcionamento                                                                                                        | Furtividade               | Compatível com Windows | Quando usar                                                                                                    |
| ------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| **SYN Scan** (Half-open) | `-sS`   | Envia pacote SYN. Se recebe SYN-ACK, a porta está aberta. Envia RST para não completar a conexão.                    | Média                     | Sim                    | É o tipo padrão e mais rápido. Ideal quando você tem privilégios de root e deseja varredura rápida e discreta. |
| **TCP Connect**          | `-sT`   | Conexão completa (SYN → SYN-ACK → ACK). Usa a pilha TCP do SO.                                                       | Baixa (fácil de detectar) | Sim                    | Quando você **não tem root** ou quer uma abordagem padrão de conexão. Fácil de detectar por firewalls.         |
| **Xmas Scan**            | `-sX`   | Envia pacotes com os bits FIN, PSH e URG ativados. Porta fechada → responde com RST. Aberta/filtrada → sem resposta. | Alta                      | Não                    | Quando deseja **escaneamento furtivo** em sistemas *Unix-like* com firewalls simples.                          |
| **Null Scan**            | `-sN`   | Envia pacotes **sem flags** TCP. Porta fechada → RST. Aberta/filtrada → sem resposta.                                | Alta                      | Não                    | Varredura silenciosa, útil contra firewalls simples. Não confiável em Windows.                                 |
| **FIN Scan**             | `-sF`   | Envia pacote com **apenas o bit FIN**. Espera RST para portas fechadas.                                              | Alta                      | Não                    | Parecido com `-sX` e `-sN`, indicado para análise furtiva em sistemas Unix.                                    |


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