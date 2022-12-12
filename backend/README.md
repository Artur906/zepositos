# Zé Pósitos: API REST em Python com banco PostgreSQL

### 0. Pré-requisitos:
* Python instalado na máquina;
* PostgreSQL rodando na máquina;
* Uma database postgres chamada de 'zepositos' (pode ser criada por meio do PgAdmim);
* VsCode (opcicional)


### 1. Instalando dependencias:
Clone este repositório em alguma pasta no seu computador.<br>
Por meio do terminal, crie um ambiente virtual python na pasta 'zepositos/backend/venv'. [Como criar ambiente virtual python?](https://www.youtube.com/watch?v=hA2l0TgaZhM)<br>
Entre no ambiente virtual.<br>
Nele, serão instaladas as seguintes dependencias:
  - Peewee (ORM)
  - Psycopg2 (Adaptador Postgres)
  - Flask (para rotas da API)
  - Flask-cors (para Cross-Origin)
  - Flask_restx (para documentação Swagger)
  - Werkzeug (WSGI)
  - Unittest (para Testes Unitarios)
  - dotenv (para configuração de variaveis de ambiente)
  
Para instalar-las, execute o comando `pip install -r requirements.txt`.


### 2. Configurando variaveis de ambiente:
Dentro da pasta 'src/settings', crie o arquivo `.env`<br>
Abra-o com um editor de texto.<br>
Nele, insira informações relativas ao PostgreSQL da sua máquina, seguindo o modelo de exemplo a seguir:<br>
```env
DATABASE_USER="postgres"
DATABASE_PASS="1234"
DATABASE_HOST="localhost"
DATABASE_PORT=5432
```
Salve o arquivo.

### 3. Rodando a API:
Rode o arquivo `main.py` (localizado na pasta src) <br>
Após isso, sua API está rodando! Observe no terminal se de fato tudo ocorreu bem. 

### 4. (opcional) Documentação SWAGGER: Como consumir a API?
Com a API rodando com sucesso, no terminal voce verá que fora _'printado'_ uma URI de acesso a API, que provavelmente se parecerá com `http://127.0.0.1:5000`. <br>
Voce pode acessar-la por meio de um navegador de internet, e será redirecionado a documentação Swagger da API.<br>
Lá são especificadas todas as rotas da API, quais métodos HTTP que podem ser usados e como, além dos modelos de dados.<br>
Esta página, além de servir de documentação, pode ser usada para testar a API, sem necessidade de ferramentas externas como o Postman.<br>
Tenha em mente que a API só pode ser consumida localmente, ou seja, na sua máquina.

### 5. (opcional) Testes Unitários: Como rodar?

Primeiro certifique-se que no seu Postgres há uma database chamada de 'zepositosTEST'.<br>
Agora rode o arquivo _runTests.py_, localizado na pasta src.<br>
Se todos os testes passarem, será mostrado no terminal uma mensagem de _OK_.

