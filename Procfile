web: python manage.py collectstatic --noinput && gunicorn -w ${GUNICORN_WORKERS:-4} gestion_tareas.wsgi:application --bind 0.0.0.0:${GUNICORN_PORT:-8000}
worker: celery -A gestion_tareas worker -l info
beat: celery -A gestion_tareas beat -l info