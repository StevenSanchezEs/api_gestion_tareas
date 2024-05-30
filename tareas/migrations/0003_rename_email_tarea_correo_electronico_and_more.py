# Generated by Django 5.0.6 on 2024-05-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_rename_fecha_vencimiento_tarea_fecha_expiracion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='email',
            new_name='correo_electronico',
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
