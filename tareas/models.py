from typing import Iterable
from django.db import models
from django.utils import timezone

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_expiracion = models.DateTimeField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    expirada = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:  # Si es una nueva tarea
            self.fecha_creacion = timezone.now()
        elif self.descripcion != self._meta.model.objects.get(pk=self.pk).descripcion or self.titulo != self._meta.model.objects.get(pk=self.pk).titulo or self.fecha_expiracion != self._meta.model.objects.get(pk=self.pk).fecha_expiracion:
            self.fecha_actualizacion = timezone.now()

        # Actualiza el campo 'expirada' basado en la fecha de expiración
        if self.fecha_expiracion and timezone.now() > self.fecha_expiracion:
            self.expirada = True
        else:
            self.expirada = False

        super().save(*args, **kwargs)