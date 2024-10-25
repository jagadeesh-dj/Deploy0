web: gunicorn chatproject.wsgi
web: python manage.py migrate && gunicorn chatproject.wsgi
web: daphne chatproject.asgi:application --port $PORT --bind 0.0.0.0
