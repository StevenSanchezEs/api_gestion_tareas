from rest_framework import status, viewsets, serializers
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from .serializers import TareaSerializer
from .tasks import enviar_notificacion_email
from .models import Tarea

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_tareas(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5  # Define el número de ítems por página
        tareas = Tarea.objects.all().order_by('-id')
        result_page = paginator.paginate_queryset(tareas, request)
        serializer = TareaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = TareaSerializer(data=request.data)
        if serializer.is_valid():
            tarea = serializer.save()
            # Enviar notificación por correo electrónico
            asunto = f'Nueva tarea creada: {tarea.titulo}'
            fecha_expiracion = "Indefinido" if tarea.fecha_expiracion is None else tarea.fecha_expiracion
            context = {
                'titulo': tarea.titulo,
                'descripcion': tarea.descripcion,
                'fecha_expiracion': fecha_expiracion,
                'enlace': "https://www.yuhu.mx"
            }
            enviar_notificacion_email.delay(email=tarea.email, subject=asunto, template_name='emails/nueva_tarea.html', context=context)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_tarea(request, pk):
    try:
        tarea = Tarea.objects.get(pk=pk)
    except Tarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TareaSerializer(tarea)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        tarea_anterior = Tarea.objects.get(pk=pk)
        serializer = TareaSerializer(tarea, data=request.data, partial=True)
        if serializer.is_valid():
            tarea_actualizada = serializer.save()

        # Comparar los datos antes y después de la actualización
        cambios = {}
        if tarea_anterior.titulo != tarea_actualizada.titulo:
            cambios['titulo'] = tarea_anterior.titulo, tarea_actualizada.titulo
        if tarea_anterior.descripcion != tarea_actualizada.descripcion:
            cambios['descripcion'] = tarea_anterior.descripcion, tarea_actualizada.descripcion
        if tarea_anterior.fecha_expiracion != tarea_actualizada.fecha_expiracion:
            cambios['fecha_expiracion'] = tarea_anterior.fecha_expiracion, tarea_actualizada.fecha_expiracion

        # Enviar notificación por correo electrónico
        if cambios:
            asunto = f'Se ha actualizado la tarea: {tarea_actualizada.titulo}'
            context = {
                'tarea_id': tarea_actualizada.id,
                'cambios': cambios
            }
            template_name = 'emails/actualizacion_tarea.html'
            enviar_notificacion_email.delay(email=tarea_actualizada.email, subject=asunto, template_name=template_name, context=context)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tarea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)