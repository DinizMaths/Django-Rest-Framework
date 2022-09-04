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
```python
INSTALLED_APPS = [..., 'rest_framework']
```
Para incluir o app como parte da aplicação, em **setup/settings.py**
```python
INSTALLED_APPS = [..., 'escola']
```
Então em seguida
`$ python manage.py makemigrations`
`$ python manage.py migrate`

Configurando admin
`$ python manage.py createsuperuser`

Dentro do app escola cria-se um **serializer.py**
```python
from rest_framework import serializers
from escola.models  import Aluno, Curso

class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aluno
    fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = '__all__'
```