# Zé Pósitos: API REST em Python com banco PostgreSQL

### 0. Pré-requisitos:
* Python instalado na máquina;
* PostgreSQL rodando na máquina;
* Uma database postgres chamada de 'zepositos' (pode ser criada por meio do PgAdmim);
* VSCode (opcional);
* Postman (opcional).


### 1. Instalando dependencias:
Crie um ambiente virtual (venv) na pasta 'backend'. [Como criar ambiente virtual python?](https://www.youtube.com/watch?v=hA2l0TgaZhM) <br>
Nele, serão instaladas as seguintes dependencias:
  - Peewee
  - Psycopg
  - Flask
  - Flask-cors
  - Flask_restx
  - Werkzeug<br>
  
Para instalar TODAS as dependencias, execute o comando `pip install -r requirements.txt`.


### 2. Configurando os arquivos:
Baixe este repositório na sua máquina.
Abra-o no VSCode.<br>
Edite o arquivo `postgredb.py` , inserindo as informações corretas relativo ao postgres rodando na sua máquina (seu usuário e senha).<br>

### 3. Deixando o banco de dados pronto para uso:
Rode o arquivo `postgredb.py`. Este script criará as tabelas **Cliente**, **Embarque** e **Volume** no seu banco de dados postgres.<br>
Olhe no seu PgAdmim na database **zepositos** para confirmar que as tabelas foram criadas.<br>

### 4. Rodando a API:
Rode o arquivo `main.py`<br>
Após isso, sua API está rodando! Observe no terminal se de fato tudo ocorreu bem. 

### 5. Consumindo a API:
Com a API rodando com sucesso, no terminal voce verá que fora _'printado'_ uma URL de acesso a API, que provavelmente se parecerá com `http://127.0.0.1:5000`. <br>
Voce pode acessar-la com um navegador de internet, e verá a mensagem _"Bem vindo a API!"_.<br>
Porém recomendo o uso da ferramenta POSTMAN para _'brincar'_ com a API, pois fica mais fácil de realizar todas as operações _CRUD_.<br>
Tenha em mente que a API só pode ser consumida localmente, ou seja, na sua máquina.

## 6. Documentação SWAGGER da API:
Certifique-se que a API está rodando na sua máquina. Se sim, a documentação poderá ser acessada na rota /docs ex: `http://127.0.0.1:5000/docs`


