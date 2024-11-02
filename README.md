<p align="center">
    <img src="https://github.com/user-attachments/assets/56ebde51-5d52-4d48-9732-444372edda3c" alt="finX" width="200" />
</p>
<h3 align="center">finX</h3>
<p align="center">Next generation cloud based multi asset complex portfolio and wealth management software platform</p>

## Project Setup

Install required packages
```
$ pip install -r requirements.txt
```

Create environment variables as suggested in ***.env.example*** file

Run migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Create superuser
```
$ python manage.py createsuperuser
```

Create public
```
$ python manage.py create_tenant --domain-domain=localhost --schema_name=public --name=Public
```

Create tenant through cmd or from admin panel (http://localhost:8000/admin-tenant)
```
$ python manage.py create_tenant --domain-domain=example.localhost --schema_name=example --name=Example
```

Fetch Nepal Stock Exchange data
```
GET request on route: http://localhost:8000/data/nepse/update-data/
```

## Used Techs
- Django
- Django Rest Framework
- Django Rest Framework SimpleJWT
- Django Tenants
- NepseUnofficialAPI
- PostgreSQL
