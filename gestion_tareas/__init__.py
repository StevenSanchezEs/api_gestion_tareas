# gestion_tareas/__init__.py
# Esto asegura que Celery se cargue cuando Django se inicia.
from .celery import app as celery_app

__all__ = ('celery_app',)