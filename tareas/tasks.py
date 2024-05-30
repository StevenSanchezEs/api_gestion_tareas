# tareas/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from decouple import config

@shared_task
def enviar_notificacion_email(email, subject, template_name, context=None):
    remitente = config('EMAIL_HOST_USER') 

    # Generar el mensaje HTML y el mensaje de texto plano
    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)

    # Enviar el correo electrónico
    send_mail(subject, plain_message, remitente, [email], html_message=html_message)
