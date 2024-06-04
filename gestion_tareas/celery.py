# gestion_tareas/celery.py
import os
from celery import Celery

# Establece el entorno de configuración predeterminado para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_tareas.settings')

app = Celery('gestion_tareas')

# Carga la configuración de Celery desde el archivo de configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-descubre las tareas en cada aplicación de Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')