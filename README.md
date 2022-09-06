# Proagro Fácil Back (Django)

Este projeto utiliza Django na versão: 4.1 e django-rest-framework na versão: 3.13.1

# Necessita das seguintes dependências:
Python https://www.python.org/
Django https://www.djangoproject.com/
PostgreSQL https://www.postgresql.org/

# Ao clonar o projeto digite os comandos a baixo
`pip install -r requirements.txt` para instalar as dependências do projeto

É necessário criar um banco de dados no postgresql com nome: `proagro`, usuario: `proagro` e senha: `'123456'` para funcionamento correto do banco de dados.
A conexão do backend django com o PSQL é feito através da url padrão: `localhost 5432`, caso necessário consultar a variável DATABASES na linha 101 do proagro-facil-back/configuracao/settings.py.
Caso necessário (dificuldades de conexão com PostgreSQL) para efeito de teste basta trocar a variável DATABASES no settings.py para a mesma variável DATABASES na linha 94 do settings.py para utilização do sqlite como teste.

`python manage.py makemigrations api`
`python manage.py migrate`
`python manage.py runserve` para rodar o projeto localmente na url/porta `http://localhost:8000/`

Ao acessar `http://localhost:8000/` através do navegador teremos a ferramenta para teste da api do django, nele é possível fazer um CRUD na entidade ComunicacaoPerda.
