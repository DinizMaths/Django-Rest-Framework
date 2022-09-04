# Django Rest Framework

Instalando Django
`$ pip3 install Django==3.0.7`

Criando projeto **setup**
`$ django-admin startproject setup .`

Dentro do arquivo **setup/settings.py**
```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```
Para rodar o projeto
`$ python manage.py runserver`

Criando app de escola
`$ python manage.py startapp escola`

Instalando **djangorestframework**
`$ pip3 install djangorestframework`

Altera-se **setup/settings.py**
`INSTALLED_APPS = [..., 'rest_framework']`