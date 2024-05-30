from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
    
    def update(self, instance, validated_data):
        # Excluimos los campos que no queremos que se actualicen
        if 'email' in validated_data:
            raise ValidationError("El campo 'email' no puede ser actualizado.")
        if 'fecha_creacion' in validated_data:
            raise ValidationError("El campo 'fecha_creacion' no puede ser actualizado.")
        if 'fecha_actualizacion' in validated_data:
            raise ValidationError("El campo 'fecha_actualizacion' no puede ser actualizado.")
        if 'expirada' in validated_data:
            raise ValidationError("El campo 'expirada' no puede ser actualizado.")

        return super().update(instance, validated_data)