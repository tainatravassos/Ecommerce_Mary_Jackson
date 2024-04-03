https://www.invertexto.com/squad - Andamento do projeto

       O que você deve fazer ao entrar no projeto pela primeira vez:

pip install virtualenv (caso não tenha o virtualenv instalado)

1- Criação do ambiente virtual: py -m venv .venv ou python -m venv .venv
2- Ativação do amb. virtual: .\.venv\Scripts\activate
3- Instalação do django: pip install django
3.1- Instalar bootstrap5 com o seguinte comando:
pip install django-bootstrap5

3.2- Intalar Pillow com comando:
python -m pip install Pillow

***Ou baixar do github e rodar o comando:***
pip install -r requirements.txt (para instalar todas as dependências do projeto de uma vez)

E após nova instalaçao para atualizar rode o comando:
pip freeze > requirements.txt

4- Para atualizar o banco de dados:
python manage.py makemigrations
python manage.py migrate

_Após garantir que o banco de dados está atualizado, você pode criar um superusuário_

6- Para criar um usuário admin:
python manage.py createsuperuser

7- Para rodar o servidor:
python manage.py runserver
http://127.0.0.1:8000/

        O que já foi feito:

- Criação do projeto:django-admin startproject projeto_ecommerce .
- Criação do app: py manage.py startapp app*MJ
  *- Criação do db.sqlite e manage.py : py manage.py makemigrations e migrate (sempre rodar esses comandos após criar um novo app ou baixar do github)\_
- Criação do requirements.txt, com os pacotes para rodar o projeto
- Criação das urls do app_MJ (home,sobre,contato)
- Criação das views do app_MJ (apenas retornando um HttpResponse)
- Criação da Models
