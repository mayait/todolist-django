from django.urls import path

from .views import (crear_proyecto, 
                    lista_proyectos, 
                    agregar_tarea,
                    detalle_proyecto,
                    editar_tarea)

from .api_views import (
                api_detalle_tarea,
                api_detalle_proyecto,
                api_lista_crear_tareas,
                api_lista_crear_proyectos
)

urlpatterns = [
    path('proyectos/', lista_proyectos, name="lista_proyectos"),
    path('proyectos/crear', crear_proyecto, name="crear_proyecto"),
    path('proyectos/<int:proyecto_id>/', detalle_proyecto, name="detalle_proyecto"),
    path('proyectos/<int:proyecto_id>/agregar-tarea/', agregar_tarea, name="agregar_tarea"),
    path('tareas/<int:tarea_id>/', editar_tarea, name="editar_tarea"),

    # API ENDPOINTS
    path('api/tareas/<int:tarea_id>/', api_detalle_tarea, name="api_detalle_tarea"),
    path('api/proyectos/', api_lista_crear_proyectos, name="api_lista_crear_proyectos"),
    path('api/proyectos/<int:proyecto_id>/', api_detalle_proyecto, name="api_detalle_proyecto"),
    path('api/proyectos/<int:proyecto_id>/tareas/', api_lista_crear_tareas, name="api_lista_crear_tareas"),
    ]