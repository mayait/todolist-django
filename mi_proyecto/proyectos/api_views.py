from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 

from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import Proyecto, Tarea, Perfil
from .serializers import TareaSerializer, ProyectoSerializer, NewTareaSerializer


@api_view(['GET','PUT','PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_detalle_tarea(request, tarea_id):
    """
    GET: Ver tarea especifica
    PUT: PATCH: Actualizar tarea
    DELETE: Elimina la tarea
    """
    tarea = get_object_or_404(Tarea, id=tarea_id)
    proyecto = tarea.proyecto

    if request.method == 'GET':
        serializer = TareaSerializer(tarea)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method in ['PUT', 'PATCH']:
        data = request.data.copy()
        serializer = TareaSerializer(tarea, data=data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if request.user == tarea.propietario:
            tarea.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT)
        
    

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_detalle_proyecto(request, proyecto_id):
    """
    GET: Detalle del proyecto
    """
    proyecto = get_object_or_404(Proyecto,id=proyecto_id
    )

    if request.method == 'GET':
        serializer = ProyectoSerializer(proyecto)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method in ['PUT', 'PATCH']:
        data = request.data.copy()
        serializer = ProyectoSerializer(proyecto, data=data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        proyecto.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def api_lista_crear_tareas(request, proyecto_id):
    """
    GET: Lista de tareas
    POST: Crea una nueva tarea
    """
    proyecto = get_object_or_404(Proyecto,id=proyecto_id)

    if request.method == 'GET':
        tareas = proyecto.tareas.all()
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data.copy()
        data['propietario'] = request.user.id
        serializer = NewTareaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def api_lista_crear_proyectos(request):
    """
    GET: Lista de proyectos
    POST: Crea una nuevo proyecto
    """
    if request.method == 'GET':
        proyectos = Proyecto.objects.all()
        serializer = ProyectoSerializer(proyectos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data.copy()
        serializer = ProyectoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
