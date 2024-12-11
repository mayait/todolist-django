# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Perfil, Proyecto, Tarea


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'avatar', 'bio')
    list_filter = ('user',)


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'descripcion',
        'fecha_creacion',
        'fecha_actualizacion',
    )
    list_filter = ('fecha_creacion', 'fecha_actualizacion')


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'proyecto',
        'titulo',
        'descripcion',
        'fecha_creacion',
        'fecha_actualizacion',
        'estado',
        'adjunto',
        'propietario',
    )
    list_filter = (
        'proyecto',
        'fecha_creacion',
        'fecha_actualizacion',
        'propietario',
    )