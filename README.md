# django-cms-sampler
====
Django cms application samples.

## Description
In this code, the following functions are implemented.
#### Administrator management function  
- list, search, register, edit

## Demo
in preparation.

## Requirement
- Python3 or more
- [requirements.txt](https://github.com/dsonoda/django-cms-sampler/blob/master/requirements.txt)

## Usage
1. test
```
$ python manage.py test
```

## Install
1. Git clone
```
$ git clone git@github.com:dsonoda/django-cms-sampler.git
```

2. Pacakges install
```
$ sudo apt-get install -y python3-pip
$ sudo apt-get install -y postgresql-9.5
$ sudo apt-get install -y python-psycopg2
$ sudo apt-get install rabbitmq-server
$ sudo service rabbitmq-server start
```
```
$ cd path/to/project
$ sudo pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

3. Database settings
```sql
postgres=# CREATE DATABASE database_name OWNER database_user ENCODING 'UTF8';
```

4. Set environment variables
```
export DJANGO_CMS_SAMPLER_DATABASE_NAME=database_name
export DJANGO_CMS_SAMPLER_DATABASE_USER=database_user
export DJANGO_CMS_SAMPLER_DATABASE_PASSWORD=database_password
export DJANGO_CMS_SAMPLER_DATABASE_HOST=localhost
export DJANGO_CMS_SAMPLER_DATABASE_PORT=5432
```

5. Django settings
```
(venv) $ django-admin startproject django_cms_sampler
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
```

6. Permission
```
chmod 777 path/to/project/media/uploads
```

7. Run set initial script
```
$ python3 path/to/django_cms_sampler/managers/django_setup.py
$ python3 path/to/django_cms_sampler/members/django_setup.py
```

8. Run server
```
(venv) $ python manage.py runserver
```

## Licence
[Apache License 2.0](https://github.com/dsonoda/django-cms-sampler/blob/master/LICENSE)

## Author
[daisuke sonoda](https://github.com/dsonoda)  
[@d5ono](https://twitter.com/d5ono)
