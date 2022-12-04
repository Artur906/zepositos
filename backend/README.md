# Zé Pósitos: API REST em Python com banco PostgreSQL

### 0. Pré-requisitos:
* Python instalado na máquina;
* PostgreSQL rodando na máquina;
* Uma database postgres chamada de 'zepositos' (pode ser criada por meio do PgAdmim);
* VSCode (opcional);
* Postman (opcional).


### 1. Configurando os arquivos:
Baixe este repositório na sua máquina.
Abra-o no VSCode.<br>
Edite o arquivo `postgredb.py` , inserindo as informações corretas relativo ao postgres rodando na sua máquina (seu usuário e senha).<br>

### 2. Instalando dependencias:
Crie um ambiente virtual (venv) na pasta 'backend'.<br>
Nele, instale as seguintes dependencias:
  - Peewee (`pip install peewee`)
  - Psycopg (`pip install psycopg2-binary`)
  - Flask (`pip install flask`)
  - Flask-cors (`pip install flask-cors`)

### 3. Deixando o banco de dados pronto para uso:
Rode o arquivo `postgredb.py`. Este script criará as tabelas **Cliente**, **Embarque** e **Volume** no seu banco de dados postgres.<br>
Olhe no seu PgAdmim na database **zepositos** para confirmar que as tabelas foram criadas.<br>

### 4. Rodando a API:
Rode o arquivo `restAPI.py`<br>
Após isso, sua API está rodando! Observe no terminal se de fato tudo ocorreu bem. 

### 5. Consumindo a API:
Com a API rodando com sucesso, no terminal voce verá que fora _'printado'_ uma URL de acesso a API, que provavelmente se parecerá com `http://127.0.0.1:5000`. <br>
Voce pode acessar-la com um navegador de internet, e verá a mensagem _"Bem vindo a API!"_.<br>
Porém recomendo o uso da ferramenta POSTMAN para _'brincar'_ com a API, pois fica mais fácil de realizar todas as operações _CRUD_.<br>
Tenha em mente que a API só pode ser consumida localmente, ou seja, na sua máquina.

## 6. Rotas da API
* ### _[URL]/_
  - Rota principal da API. Retorna a mensagem "Bem vindo a API!".

<br>

* ### _[URL]/clientes_
  - **GET**: Retorna TODOS os clientes.
  - **POST**: Deve ser enviado a API um json de um novo cliente a ser ADICIONADO:
    - ```bash 
      {
        "nome": "Meujarel", 
        "telefone": 111111111
      }
      ```
    - Se a operação ocorrer com sucesso, retorna o id do novo cliente inserido no banco e um código de sucesso 201.
    
<br>

* ### _[URL]/clientes/[id]_
  - **GET**: Retorna o json do cliente dono do id.
  - **PATCH**: Deve ser informado na URL o id do cliente a ser ATUALIZADO, como também um json das novas informações deste cliente
    - ```bash 
      {
        "nome": "Meljael"
      }
      ```
    - Retorna uma mensagem de sucesso (código 200) caso ocorra tudo bem.
  
   - **DELETE**:  Deve ser informado na URL o id do cliente a ser DELETADO.
     - Retorna uma mensagem de sucesso (código 200) caso ocorra tudo bem.


