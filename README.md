# Alguns comandos do git 

### COMANDOS BÁSICOS

#### clonar reposítório
```bash 
git clone https://github.com/usuario/nomedorepo.git
```
#### adicionar arquivos modificados ao git local
```bash 
git add .
```
a gente pode colocar um arquivo específico, mas eu sempre adiciono todos de uma vez usando o ponto

#### fazendo o commit
```bash 
git commit -m -a "aqui eu descrevo minhas modificações"
```
o -a serve para adicioanr todos os arquivos modificados automaticamente para o commit, sem a necessidade de `git add ,`
#### subindo as modificações para o repositório na web
```bash 
git push
```
#### atualizando nossa branch local pegando do repositório no github
```bash 
git pull
```

### MANIPULANDO BRANCHS

#### listar todas as branchs
```bash
git branch
``` 
#### criar nova branch
```bash
git branch nome-da-branch
``` 
#### trocar de branch
```bash
git checkout nome-da-branch
``` 
#### atalho 
podemos juntar os ultimos dois comandos em um só, no caso criamos e trocamos de branch na mesma hora
```bash
git checkout -b nome-da-branch
```

#### apagando branch 
esqueci de falar no vídeo mas dá pra apagar as branchs locais também 
```bash 
git branch -d nome-da-branch
``` 
