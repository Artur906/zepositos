# Zé Pósitos: API REST em Python com banco PostgreSQL
## Como rodar o backend?
Voce pode seguir os passos descritos abaixo, ou ver este [video](https://youtu.be/x9d15Am9EMI) tutorial de 3 minutos.
### 0. Pré-requisitos:
* Python instalado;
* PostgreSQL rodando na máquina;
* Uma database chamada de _"zepositos"_ (pode ser criada por meio do PgAdmim);


### 1. Instalando dependencias:
Clone este repositório em alguma pasta no seu computador.<br>
Abra o terminal.<br>
Navegue até a pasta do _backend_, e nela crie um ambiente virtual python (pode ficar numa pasta _venv_).<br>
Ative o ambiente virtual.<br>

<details>
  <summary>Nele, serão instaladas as seguintes dependencias:</summary>
  
  - Peewee (ORM)
  - Psycopg2 (Adaptador Postgres)
  - Flask (para rotas da API)
  - Flask-cors (para Cross-Origin)
  - Flask_restx (para documentação Swagger)
  - Werkzeug (WSGI)
  - Unittest (para Testes Unitarios)
  - dotenv (para configuração de variaveis de ambiente)
</details>

Para instalar-las, dentro da pasta do backend execute o comando <br>`pip install -r requirements.txt`.


### 2. Configurando variaveis de ambiente:
Dentro da pasta _"zepositos/backend/src/settings"_, crie o arquivo **.env**<br>
Abra-o com um editor de texto.<br>
Nele, insira informações relativas ao seu PostgreSQL, seguindo o modelo a seguir de exemplo:<br>
```env
DATABASE_USER="postgres"
DATABASE_PASS="1234"
DATABASE_HOST="localhost"
DATABASE_PORT=5432
```
Salve o arquivo.

## 3. Rodando a API:
Por meio do terminal, ative o ambiente virtual criado no primeiro passo.<br>
Navegue para dentro da pasta _"zepositos/backend"_, e execute o comando<br> `python main.py` <br>
Após isso, a API do ZéPósitos estará conectada com o seu banco de dados e pronta para ser consumida pelo frontend!<br> 


***
Abaixo estão ações **opcionais** que não precisam ser realizadas para que o backend funcione.


#### Como rodar pelo VsCode?
(Certifique-se que tem a [extensão do python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) instalada)<br>
Abra a pasta _zepositos_ no seu VsCode;<br>
Ctrl+Shift+P e pesquise _"Selecionar Interpretador (Python)"_;<br>
Escolha a opção _"Insira o caminho do interpretador"_->_"Localizar"_;<br>
Isso abrirá o seu explorador de arquivos. Selecione o executavel python localizado no seu ambiente virtual<br> 
ex: _zepositos/backend/venv/Scripts/python.exe_;<br>
Pronto, agora no VsCode é só rodar o arquivo **main.py** localizado na pasta do _backend_. 

#### Documentação SWAGGER: Como consumir a API?
Com a API rodando com sucesso, no terminal voce verá que fora _'printado'_ uma URI de acesso local a API (`http://127.0.0.1:5000`). <br>
Voce pode acessar-la por meio de um navegador de internet, onde será redirecionado a documentação da API.<br>
Lá são especificadas todas as rotas da API, os modelos dos dados, além de quais os métodos HTTP que podem ser usados e como devem.<br>
Esta página, além de servir de documentação, pode ser usada para testar a API, sem necessidade de ferramentas externas como o Postman.<br>
Tenha em mente que a API está configurada para ser acessada apenas localmente na sua máquina.

#### Testes Unitários: Como rodar?
Primeiro certifique-se que no seu Postgres há uma database chamada de _"zepositosTEST"_.<br>
Agora rode o arquivo **runTests.py**<br>
Se todos os testes passarem, será mostrado no terminal uma mensagem de _OK_.
