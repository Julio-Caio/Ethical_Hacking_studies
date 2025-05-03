## Masscan

- É utilizado para enumerar hosts e serviços de forma **massiva** em redes, permitindo uma varredura **Muito rápida**, dependendo de sua taxa (--rate) e banda disponível.

- Utilizado quando você pensa mais em **velocidade**, e não furtividade.

- Utiliza em seu scanning, pacotes brutos **SYN** do TCP, e quando o host envia um SYN/ACK, interpreta que a porta está **aberta**.

- Pela popularidade do nmap em serviços de scanning, optou-se por utilizar os mesmos parâmetros

### --rate

- A diferença principal é o parâmetro **--rate**, onde indica o número de **pacotes a cada 1 segundo**
- Exemplo:
    - Imagine que você queira realizar uma varredura usando 2 pacotes p/segundo, você utilizaria
        
        ```
        sudo masscan -- rate=0.5 -p80,443 192.168.86.0/24
        ``` 
    - Ou seja, 1 pacote a cada 2 segundos = 1/2 = 0.5
    - 100.000 pacotes por segundos = 100.000
    ...

#### --randomized-hosts

Neste parâmetro, o masscan irá scanear todos os hosts daquela rede, de forma **NÃO SEQUENCIAL**, evitando-se uma detectção instâtanea por IPS, Firewalls.

### --banners

Ao especificar as portas, o masscan irá obter os headers obtidos naquele serviço, se o serviço não responder nada, não considera um servidor válido.

```
sudo masscan -sS -- banners -- rate=100000 -p80,443 192.168.86.0/24
```

### Limitações

- O masscan não tem tantas funcionalidades em comparação ao nmap, como os diversos tipos de scanning como o Xmas, FYN e ACK.
- Ele **não suporta UDP**
