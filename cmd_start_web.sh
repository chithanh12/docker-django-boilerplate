#while ! nc -w 1 -z db 5432; do sleep 0.1; done
python manage.py migrate
python manage.py runserver 0.0.0.0:80