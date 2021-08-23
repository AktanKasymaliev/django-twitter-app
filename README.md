# django-twitter-app
We did this project when we were begginers
Hello, in the first, you sould clone rep:
* cloning repository:
```
git clone https://github.com/AktanKasymaliev/django-twitter-app.git
```
* Download virtual enviroment:
```
pip install python3-venv 
Activating: python3 -m venv venv
```
* Install all requirements: 
```
pip install -r requirements.txt
```

* Create a file .env on self project level, copy under text, and add your value: 
```
SECRET_KEY = 
DEBUG = 
DB_PASSWORD = 
DB_USER = 
DB_NAME = 
```
* Sync database with Django:
```
- python manage.py makemigrations
- python manage.py migrate
```

* Create superuser
```
- python manage.py createsuperuser
```
