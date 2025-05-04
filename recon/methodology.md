# 🕵️ Guia de Reconhecimento em Pentest – Metodologia + Checklist

## 🔍 Fase 1 – Reconhecimento Passivo

### ✅ Objetivos:
- Obter informações sem interagir diretamente com o alvo.
- Mapear domínios, subdomínios, IPs, ASN e tecnologias.

### 📋 Checklist:

- [ ] Buscar domínios e subdomínios:
  - CRT.sh
  - Sublist3r
  - Assetfinder
  - Amass
- [ ] Coletar registros DNS (A, MX, NS, TXT)
- [ ] Usar Google Dorks para buscar arquivos expostos
- [ ] Buscar metadados em PDFs, DOCs, PPTs com FOCA
- [ ] Buscar leaks em:
  - Pastebin
  - GitHub
  - Wayback Machine
- [ ] Verificar dados expostos em redes sociais
- [ ] Coletar ASN, blocos IP, WHOIS

### 🔧 Ferramentas:
Amass, theHarvester, FOCA, SecurityTrails, Shodan, Censys, Google
---

## 🧭 Fase 2 – Reconhecimento Ativo

### ✅ Objetivos:
- Identificar hosts vivos, portas abertas e serviços.

### 📋 Checklist:

- [ ] Descobrir hosts ativos (ping sweep, DNS reverso)
- [ ] Scan de portas:
  - Nmap (TCP e UDP)
  - Masscan / ZMap para grandes redes
- [ ] Identificar serviços (banner grabbing, `nmap -sV`)
- [ ] Detectar SO (`nmap -O`)
- [ ] Testar bypass de firewall e evasão
- [ ] Detectar presença de WAF

### 🔧 Ferramentas:
Nmap, Masscan, ZMap, Netcat, Telnet, WhatWeb, Wappalyzer

---

## 🧱 Fase 3 – Enumeração de Serviços

### ✅ Objetivos:
- Obter detalhes de serviços específicos.
- Encontrar pontos vulneráveis.

### 📋 Checklist:

#### HTTP/HTTPS:
- [ ] Enumeração de diretórios (Gobuster, Dirsearch)
- [ ] Identificação de tecnologias (WhatWeb, Wappalyzer)
- [ ] Coleta de headers HTTP
- [ ] Verificar arquivos como:
  - robots.txt
  - sitemap.xml
  - .git, .env
- [ ] Fuzzing com ffuf, wfuzz, Burp Suite

#### SMB:
- [ ] Listar compartilhamentos (`smbclient -L`)
- [ ] Enumeração com enum4linux / CrackMapExec
- [ ] Testar login anônimo

#### FTP:
- [ ] Testar login anônimo
- [ ] Baixar arquivos disponíveis

#### DNS:
- [ ] Testar zone transfer (`dig axfr`)
- [ ] Brute-force de subdomínios

#### SSH:
- [ ] Verificar políticas de autenticação
- [ ] Coletar banner / versão
- [ ] Testar brute-force (Hydra, Patator)

#### Bancos de Dados:
- [ ] Identificar MySQL, PostgreSQL, Redis, etc.
- [ ] Testar acesso sem autenticação
- [ ] Coletar banners

#### SNMP:
- [ ] Testar com `snmpwalk -c public`
- [ ] Coletar informações de rede e usuários

#### SMTP:
- [ ] Verificar VRFY/EXPN para enumeração de usuários
- [ ] Testar relay aberto

#### Outros:
- [ ] RDP
- [ ] VNC
- [ ] Telnet
- [ ] LDAP
- [ ] Elasticsearch

### 🔧 Ferramentas:
Enum4linux, CrackMapExec, Gobuster, ffuf, Dirsearch, Hydra, Snmpwalk, Nikto, Nuclei, Searchsploit

---

## 📦 Checklist Final – Informações Coletadas

| Dado                                          | Status |
|---------------------------------------------- |--------|
| [ ] Endereços IP válidos e ativos             |        |
| [ ] Portas abertas e serviços identificados   |        |
| [ ] Sistemas operacionais identificados       |        |
| [ ] Subdomínios e domínios associados         |        |
| [ ] Tecnologias Web e CMS detectados          |        |
| [ ] Serviços vulneráveis / versões antigas    |        |
| [ ] Arquivos sensíveis (.git, .env, etc.)     |        |
| [ ] Credenciais fracas (FTP, SMB, SSH, etc.)  |        |
| [ ] Potenciais pontos de entrada              |        |

---

**⚠️ Observação:** Sempre realize o reconhecimento ativo apenas com autorização. Reconhecimento não autorizado pode ser considerado ilegal.