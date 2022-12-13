# Zé Pósitos: API REST em Python com banco PostgreSQL


### 0. Pré-requisitos:
* Python instalado na máquina;
* PostgreSQL rodando na máquina;
* Uma database postgres chamada de 'zepositos' (pode ser criada por meio do PgAdmim);
* VsCode (opcicional)


### 1. Instalando dependencias:
Clone este repositório em alguma pasta no seu computador.<br>
Por meio do terminal, crie um ambiente virtual python na pasta do backend. <br> (ex: `python -m venv venv`) [Como criar ambiente virtual python?](https://www.youtube.com/watch?v=hA2l0TgaZhM)<br>
Ative o ambiente virtual (`./Scripts/activate`).<br>
Nele, serão instaladas as seguintes dependencias:
  - Peewee (ORM)
  - Psycopg2 (Adaptador Postgres)
  - Flask (para rotas da API)
  - Flask-cors (para Cross-Origin)
  - Flask_restx (para documentação Swagger)
  - Werkzeug (WSGI)
  - Unittest (para Testes Unitarios)
  - dotenv (para configuração de variaveis de ambiente)
  
Para instalar-las, entre na pasta do backend e execute o comando `pip install -r requirements.txt`.


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
Por meio do terminal, ative o ambiente virtual do zepositos.<br>
Dentro da pasta do backend, execute o comando `python main.py` <br>
Após isso, sua API está rodando! Observe no terminal se de fato tudo ocorreu bem. 

#### 3.1 (Opcional) Como rodar pelo VsCode?
Abra a pasta do zepositos no seu vscode.<br>
Certifique-se que tem a [extensão do python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) instalada no vscode.<br>
Ctrl+Shift+P e Pesquise "Selecionar Interpretador (Python)"<br>
Escolha a opção "Insira o caminho do interpretador"->"Localizar".<br>
Isso abrirá o seu explorador de arquivos. Selecione o executavel python localizado no seu ambiente virtual (ex: venv/Scripts/python.exe).<br>
Pronto, agora no VsCode é só rodar o arquivo main.py .

### 4. (Opcional) Documentação SWAGGER: Como consumir a API?
Com a API rodando com sucesso, no terminal voce verá que fora _'printado'_ uma URI de acesso a API, que provavelmente se parecerá com `http://127.0.0.1:5000`. <br>
Voce pode acessar-la por meio de um navegador de internet, e será redirecionado a documentação Swagger da API.<br>
Lá são especificadas todas as rotas da API, quais métodos HTTP que podem ser usados e como, além dos modelos de dados.<br>
Esta página, além de servir de documentação, pode ser usada para testar a API, sem necessidade de ferramentas externas como o Postman.<br>
Tenha em mente que a API só pode ser consumida localmente, ou seja, na sua máquina.

### 5. (Opcional) Testes Unitários: Como rodar?

Primeiro certifique-se que no seu Postgres há uma database chamada de 'zepositosTEST'.<br>
Agora rode o arquivo _runTests.py_.<br>
Se todos os testes passarem, será mostrado no terminal uma mensagem de _OK_.

