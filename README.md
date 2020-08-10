# Simple text analyzer created with Django

### There are two pages:

```/``` - index page that shows you amount of each word

```/create/``` page allows you to enter some text and get it counted

### Steps to install:

Clone project:

    git clone https://github.com/dev-yaroslav-b/django-simple-text-analyzer.git


Create virtual environment:

    virtualenv --python=python3.7 venv


Activate venv ```source venv/bin/activate``` and install requirements:

    pip install -r requirements.txt

Create db and run migrations:

    python manage.py makemigrations
    python manage.py migrate
    
Run server:

    python manage.py runserver
    

    
