from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Proyecto, Tarea

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',

        ]

class TareaSerializer(serializers.ModelSerializer):
    propietario = PropietarioSerializer()
    class Meta:
        model = Tarea
        fields = [
            'id',
            'titulo',
            'descripcion',
            'estado',
            'adjunto',
            'proyecto',
            'propietario',
        ]
        read_only_fields = [
            'fecha_creacion', 
            'fecha_modificacion'
            ]

class NewTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = [
            'id',
            'titulo',
            'descripcion',
            'estado',
            'adjunto',
            'proyecto',
            'propietario',
        ]
        read_only_fields = [
            'fecha_creacion', 
            'fecha_modificacion'
            ]
        
class ProyectoSerializer(serializers.ModelSerializer):
    tareas = TareaSerializer(many=True, read_only=True)
    class Meta:
        model = Proyecto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'tareas'
            
        ]
        read_only_fields = [
            'fecha_creacion', 
            'fecha_modificacion'
            ]