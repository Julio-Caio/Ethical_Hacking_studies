<h1>Vulnerabilidades</h1>

**O que é uma Vulnerabilidade?**

Segundo a NIST, é uma falha/fraqueza em um sistema de informação, procedimentos do sistema de segurança, controles internos ou uma implementação, que pode ser explorada por uma ameaça.

| **Vulnerabilidade**             | **Descrição**                                                                                                                                                                 |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sistema Operacional**        | Esse tipo de vulnerabilidade é encontrado em sistemas operacionais e frequentemente resulta em escalonamento de privilégios.                                               |
| **(Má) Configuração**          | Esse tipo de vulnerabilidade surge de uma aplicação ou serviço mal configurado. Por exemplo, um site que expõe dados de clientes.                                          |
| **Credenciais Fracas ou Padrão** | Aplicações e serviços que possuem autenticação costumam vir com credenciais padrão após a instalação. Por exemplo, um painel administrativo com usuário e senha "admin". Essas são facilmente adivinhadas por um atacante. |
| **Lógica da Aplicação**        | Essas vulnerabilidades são resultado de aplicações mal projetadas. Por exemplo, mecanismos de autenticação mal implementados que permitem a um atacante se passar por outro usuário. |
| **Fator Humano**               | Vulnerabilidades que exploram o comportamento humano. Por exemplo, e-mails de phishing criados para enganar usuários e fazê-los acreditar que são legítimos.               |

---
<br>

## Gerenciamento de Vulnerabilidades

O gerenciamento de vulnerabilidades é o processo de **avaliar, categorizar e, por fim, remediar ameaças** (vulnerabilidades) enfrentadas por uma organização.

É praticamente impossível corrigir todas as vulnerabilidades existentes em uma rede ou sistema computacional — e, em alguns casos, isso pode representar um desperdício de recursos.

Afinal, **apenas cerca de 2% das vulnerabilidades chegam a ser exploradas** (Kenna Security, 2020). Por isso, o foco deve ser em lidar com as vulnerabilidades mais perigosas e **reduzir a probabilidade de um vetor de ataque ser utilizado para explorar um sistema**.

É aqui que entra a **pontuação de vulnerabilidades**. Ela desempenha um papel essencial no gerenciamento de vulnerabilidades, pois serve para determinar o **potencial de risco e impacto** que uma vulnerabilidade pode ter sobre uma rede ou sistema computacional.

Por exemplo, o popular **Sistema Comum de Pontuação de Vulnerabilidades (CVSS)** atribui pontos a uma vulnerabilidade com base em fatores como suas características, disponibilidade e reprodutibilidade.

Claro, como em muitas áreas da TI, **não existe apenas um framework ou metodologia proposta**. Vamos explorar dois dos frameworks mais comuns e analisar como eles se diferenciam.

---

### Sistema Comum de Pontuação de Vulnerabilidades (CVSS)

- Introduzido pela primeira vez em 2005, o **Common Vulnerability Scoring System (CVSS)** é um dos frameworks mais populares para pontuação de vulnerabilidades e possui três grandes versões.

- É gratuito e recomendado pela **NIST**

- Atualmente, a versão vigente é a **CVSS v3.1** (com a versão 4.0 em fase de rascunho). A pontuação de uma vulnerabilidade é essencialmente determinada por diversos fatores, incluindo (mas não se limitando a):

1. **Quão fácil é explorar a vulnerabilidade?**
2. **Existem exploits disponíveis para essa vulnerabilidade?**
3. **Como essa vulnerabilidade afeta a tríade CIA (Confidencialidade, Integridade e Disponibilidade)?**

<h3>Links Úteis</h3>

**CVSS v3 Calculator**

[Acesse a calculadora CVSS aqui](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator#)


### VPR

O VPR é um dos frameworks de gerenciamento de vulnerabilidades mais modernos, desenvolvido pela Tenable, um provedor de soluções na área de gerenciamento de vulnerabilidades.

#### Características

- **Não é open-source**

- **Risk-Driven**: a pontuação VPR leva em consideração a relevância de uma vulnerabilidade. Por exemplo, nenhum risco é considerado em relação a uma vulnerabilidade se ela não se aplica à organização (ou seja, se a empresa não utiliza o software vulnerável).

- **Dinâmico**:  o risco que uma vulnerabilidade pode representar pode mudar quase diariamente conforme ela envelhece.

- Embora o VPR tenha um foco mais forte no risco específico para a organização, ele ainda leva em consideração fatores relacionados à segurança, incluindo aspectos da tríade CIA. No entanto, o risco é avaliado de forma mais contextualizada e baseada na relevância para a organização, ao invés de atribuir uma pontuação direta como o CVSS.

---
<br>

### CVE

Todas as vulnerabilidades no NVD (National Vulnerability Database), este que é administrado pela NIST, possui um identificador CVE.

O CVE define uma vulnerabilidade como um:

- " A falha na lógica computacional (ex.: código) presente em componente(s) de um software ou hardware, que, se explorada, pode resultar em impactos negativos na confidencialidade, integridade ou disponibilidade."

A mitigação de vulnerabilidades, nestes casos, pode envolver: mudanças no código-fonte, especificações de mudanças, ou especificar remoções (remover desde protocolos até em uma funcionalidade)