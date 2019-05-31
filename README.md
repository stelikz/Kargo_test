To Set Up

source .env

```
createdb test_db
createdb flask_api

pip install Flask

pip install flask_sqlalchemy

pip install flask_script
pip install flask_migrate
pip install psycopg2-binary
pip install flask_api
python manage.py db init

python manage.py db migrate

python manage.py db upgrade

pip install Flask-API
```

To Run the App

```
flask run
```

To Run the Test

```
python test.py
```
