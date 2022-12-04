Certifique-se que a pasta 'backend' deste repositorio na sua máquina é um ambiente virtual python (venv).<br>
Então instale as seguintes Dependencias:<br>
- `pip install unittest2`
- `pip install peewee`
- `pip install psycopg2-binary`

Para executar os testes unitário, rode o arquivo `unitTests.py`.<br>
Mas antes disso, certifique-se de que o seu postgres está aberto e que voce criou uma database exclusiva para os testes chamada **zepositosTEST**.<br>
Certifique-se também que no arquivo `testPostgreDB.py` estão informados o SEU **usuario e senha**. <br>
Os testes são independentes da API, ou seja, ela não precisa estar rodando.
