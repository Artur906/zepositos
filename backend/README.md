# Zé Pósitos: API REST em Python com banco PostgreSQL

### 0. Pré-requisitos:
* Python instalado na máquina;
* PostgreSQL rodando na máquina;
* Uma database postgres chamada de 'zepositos' (pode ser criada por meio do PgAdmim);
* VsCode (opcicional)


### 1. Instalando dependencias:
Por meio do terminal, crie um ambiente virtual (venv) na pasta 'venv'. [Como criar ambiente virtual python?](https://www.youtube.com/watch?v=hA2l0TgaZhM)<br>
Entre no ambiente virtual.<br>
Nele, serão instaladas as seguintes dependencias:
  - Peewee (ORM)
  - Psycopg2 (Adaptador Postgres)
  - Flask (para rotas da API)
  - Flask-cors (para Cross-Origin)
  - Flask_restx (para documentação Swagger)
  - Werkzeug (WSGI) <br>
Para instalar-las, execute o comando `pip install -r requirements.txt`.


### 2. Configurando os arquivos:
Baixe este repositório e salve em alguma pasta no seu computador.<br>
Abra-a no VSCode.<br>
Insira no arquivo `postgredb.py` (localizado em src/server) as informações do postgres rodando na sua máquina (seu usuário e senha).<br>

### 3. Rodando a API:
Rode o arquivo `main.py` (localizado em src) <br>
Após isso, sua API está rodando! Observe no terminal se de fato tudo ocorreu bem. 

### 4. Consumindo a API:
Com a API rodando com sucesso, no terminal voce verá que fora _'printado'_ uma URL de acesso a API, que provavelmente se parecerá com `http://127.0.0.1:5000`. <br>
Voce pode acessar-la por meio de um navegador de internet, e entrará na documentação da API.<br>
Tenha em mente que a API só pode ser consumida localmente, ou seja, na sua máquina.

## 5. Documentação SWAGGER da API:
Certifique-se que a API já está rodando na sua máquina. Se sim, a documentação poderá ser acessada em uma págnina localizada na rota / <br>
ex: `http://127.0.0.1:5000`<br>
Esta página, além de servir de documentação, pode ser usada para testar a API, sem necessidade de ferramentas externas como o Postman.


