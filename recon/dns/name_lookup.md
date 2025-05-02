## 🔹 **O que é um servidor DNS de cache?**

### 📌 **Como ele funciona?**

Um servidor **DNS de cache** (ou recursivo) é responsável por **resolver nomes de domínio** em endereços IP **consultando outros servidores DNS** e **armazenando as respostas temporariamente** (em cache) para acelerar futuras resoluções.

### 🔄 **Processo de recursão — exemplo básico:**

Imagine que você quer acessar `www.exemplo.com`. Seu computador faz a requisição para o servidor DNS de cache configurado (geralmente do seu provedor de internet ou empresa). O processo é assim:

1. **Seu computador pergunta:** "Qual o IP de `www.exemplo.com`?"
2. O **servidor DNS de cache** verifica se já tem essa informação em cache:
   - Se **sim**, ele retorna o IP imediatamente.
   - Se **não**, ele inicia uma **consulta recursiva**:
     - Pergunta a um **servidor root**: “Quem sabe sobre `.com`?”
     - O root responde: “Pergunte ao servidor TLD (Top-Level Domain) responsável por `.com`”.
     - O cache pergunta ao servidor TLD: “Quem sabe sobre `exemplo.com`?”
     - O TLD responde com o endereço do **servidor autoritativo** de `exemplo.com`.
     - O cache então pergunta a esse servidor autoritativo: “Qual o IP de `www.exemplo.com`?”
     - Ele recebe a resposta final, por exemplo: `192.0.2.1`.
3. O **servidor DNS de cache armazena (cacha) a resposta** por um tempo (TTL).
4. Retorna o IP para seu computador, que então acessa o site.

### 👥 **Quem o utiliza na prática?**
- **Usuários finais**, indiretamente (por meio do provedor de internet).
- **Empresas**, que muitas vezes mantêm servidores DNS recursivos internos.
- **Serviços públicos**, como o **Google DNS (8.8.8.8)** e **Cloudflare DNS (1.1.1.1)**.

---

## 🔹 **O que é um servidor DNS autoritativo?**

### 📌 **Como ele funciona?**

Um **servidor DNS autoritativo** **contém as informações oficiais** (registros) sobre um determinado domínio, como:

- Registros **A** (nome → IPv4),
- Registros **MX** (e-mails),
- Registros **CNAME**, **NS**, entre outros.

Ele **não faz consultas recursivas**. Ele **responde com autoridade** quando alguém pergunta algo sobre um domínio que ele gerencia.

### 🛠️ **O que ele resolve na prática?**

Ele responde **com os dados originais e finais** sobre domínios. Por exemplo:

- Quando o servidor recursivo quer saber o IP de `www.exemplo.com`, o autoritativo de `exemplo.com` fornece o IP.
- Essencial para que sites, e-mails e outros serviços de internet funcionem corretamente.

### ✅ Exemplo:
O domínio `empresa.com.br` pode ter servidores autoritativos configurados como:
- `ns1.empresa.com.br`
- `ns2.empresa.com.br`

Se alguém quiser saber o IP de `www.empresa.com.br`, o servidor autoritativo de `empresa.com.br` dará a resposta.

---

## 🔹 **O que é um servidor DNS root?**

### 🌍 **O papel do root server:**
É o **nível mais alto da hierarquia DNS**. Ele **não sabe os IPs de todos os domínios**, mas sabe onde estão os **servidores TLDs** (como `.com`, `.org`, `.br`, etc.).

### 📡 **Como funciona na prática?**

Quando um servidor recursivo não sabe nada (consulta "fria"), ele **começa perguntando ao root**. Por exemplo:

- “Quem é responsável pelo domínio `.org`?”
- O root responde: “Veja estes servidores TLD para `.org`...”

### 🌐 **13 root servers — o que isso significa?**

Existem **13 identificadores de servidores root**, nomeados de **A a M** (como `a.root-servers.net`, `b.root-servers.net`, ..., `m.root-servers.net`).  
Mas **não são apenas 13 máquinas** — na verdade, **há centenas de réplicas (espelhamentos)** no mundo todo via **Anycast**, para garantir disponibilidade e distribuição geográfica.