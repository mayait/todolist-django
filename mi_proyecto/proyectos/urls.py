from django.urls import path

from .views import (crear_proyecto, 
                    lista_proyectos, 
                    agregar_tarea,
                    detalle_proyecto,
                    editar_tarea)

urlpatterns = [
    path('proyectos/', lista_proyectos, name="lista_proyectos"),
    path('proyectos/crear', crear_proyecto, name="crear_proyecto"),
    path('proyectos/<int:proyecto_id>/', detalle_proyecto, name="detalle_proyecto"),
    path('proyectos/<int:proyecto_id>/agregar-tarea/', agregar_tarea, name="agregar_tarea"),
    path('tareas/<int:tarea_id>/', editar_tarea, name="editar_tarea"),

]