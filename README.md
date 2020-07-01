gunicorn --worker-class gevent -b 0.0.0.0 -p 8000 mysite.wsgi

or

daphne -b 0.0.0.0 -p 8000 mysite.asgi:application