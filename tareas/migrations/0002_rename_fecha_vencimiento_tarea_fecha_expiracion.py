# Generated by Django 5.0.6 on 2024-05-29 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='fecha_vencimiento',
            new_name='fecha_expiracion',
        ),
    ]
