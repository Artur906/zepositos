# Exemplo de uma API REST Python com banco PostgreSQL

### 0. Pré-requisitos:
* Python instalado na máquina
* VSCode instalado
* PostgreSQL rodando na máquina
* Uma nova database criada no PGAdmim para o teste
* Ambiente virtual python (venv) com:
  - Peewee (`pip install peewee`)
  - Psycopg (`pip install psycopg2-binary`)
  - Flask (`pip install flask`)
  - Flask-cors (`pip install flask-cors`)
* Postman (opcional)


### 1. Configurando os arquivos:
Baixe todos os arquivos .py presentes na pasta deste repositório e coloque os na pasta do ambiente virtual que voce criou.<br>
Abra-a no VSCode.<br>
Edite o arquivo `postgredb.py` , inserindo as informações corretas relativo ao postgre rodando na sua máquina (senha, usuário, nome da database que voce criou).<br>

### 2. Deixando o banco de dados pronto para uso:
Rode o arquivo `esquema.py`. Este script criará a tabela 'clientes' no seu postgre. Olhe no seu PgAdmim para confirmar que a tabela foi criada.<br>
Rode o arquivo `inserir-dados.py`. Este script insere tres clientes na tabela.<br>

### 3. Rodando a API:
Agora chegou a hora de usar o arquivo `backendAPI.py` para de fato deixar a API funcionando localmente.<br>
Para tal, é necessário rodar os seguintes comandos no terminal do VsCode:

```bash 
export FLASK_APP=backendAPI.py
export FLASK_DEBUG=1
flask run
```
Após isso, sua API está rodando! Observe no terminal se de fato tudo ocorreu bem. 

### 4. Consumindo a API:
Com a API rodando com sucesso, no terminal voce verá que fora _'printado'_ uma URL de acesso a API. <br>
Voce pode acessar-la com um navegador de internet, e verá a mensagem _"Bem vindo a API!"_.<br>
Porém recomendo o uso da ferramenta POSTMAN para _'brincar'_ com a API, pois fica mais fácil de realizar todas as operações _CRUD_.<br>
Tenha em mente que a API só pode ser consumida localmente, ou seja, na sua máquina.

## 5. Rotas da API
* ### _[URL]/_
  - Rota principal da API. Retorna a mensagem "bem vindo a API!".

<br>

* ### _[URL]/clientes_
  - **GET**: Retorna TODOS os clientes.
  - **POST**: Deve ser enviado a API um json de um novo cliente a ser ADICIONADO:
    - ```bash 
      {
        "nome": "Meujarel"
      }
      ```
    - Se a operação ocorrer com sucesso, retorna o id do novo cliente inserido no banco.
    
<br>

* ### _[URL]/clientes/[id]_
  - **GET**: Retorna o json do cliente dono do id.
  - **PUT**: Deve ser informado na URL o id do cliente a ser ATUALIZADO, como também um json das novas informações deste cliente
    - ```bash 
      {
        "nome": "Meljael"
      }
      ```
    - Retorna uma mensagem de sucesso (código 200) caso ocorra tudo bem.
  
   - **DELETE**:  Deve ser informado na URL o id do cliente a ser DELETADO.
     - Retorna uma mensagem de sucesso (código 200) caso ocorra tudo bem.




