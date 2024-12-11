from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# importamos los modelos
from .models import Proyecto, Tarea, Perfil
# importamos los formularios
from .forms import ProyectoForm, TareaForm, TareaFormSet

@login_required
def crear_proyecto(request):
    """
    Vista para crear un proyecto nuevo.
    Permite añaidr tareas al mismo tiempo.
    """

    if request.method == 'POST':
        proyecto_form = ProyectoForm(request.POST, request.FILES)
        tarea_formset = TareaFormSet(request.POST, request.FILES, prefix='tareas', instance=Proyecto())

        if proyecto_form.is_valid() and tarea_formset.is_valid():
            # Guardar el proyecto en varios objetos
            proyecto = proyecto_form.save(commit=False) # commit = False no guarda el objeto en la base de datos todavia
            # modifica todos los elementos que quieras del objeto antes de guardar.
            proyecto.save()
            
            # Guardar las tareas del formset
            tareas = tarea_formset.save(commit=False) # No guardes todavia en la bbdd
            # iterar sobre las tareas
            for tarea in tareas:
                tarea.proyecto = proyecto # Guardale el proyecto que le acabas de crear
                tarea.propietario = request.user
                # modifica todos los elementos que quieras del objeto antes de guardar.
                tarea.save()
            return redirect('lista_proyectos')
    else:
        # si el metodo es GET, por que no es POST, crea formularios vacios.
        proyecto_form = ProyectoForm()
        tarea_formset = TareaFormSet(prefix='tareas')
    
    # Pilas no te olvides de pasar el contexto
    contexto = {
        'proyecto_form': proyecto_form,
        'tarea_formset': tarea_formset
    }

    return render(request, 'crear_proyecto.html', contexto)


@login_required
def lista_proyectos(request):
    propietario = request.user # El usuario loggeado
    # Filtra solo los proyectos del usuario activo
    proyectos = Proyecto.objects.all()
    # Pilas no te olvides de pasar el contexto
    contexto = {
        'proyectos': proyectos,
    }
    return render(request, 'lista_proyectos.html', contexto)


@login_required
def agregar_tarea(request, proyecto_id):
    # Toda tarea necesita un proyecto
    # Busquemos un proyecto
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, request.FILES)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.propietario = request.user
            tarea.save()
            return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)
    else:
        # Si el metodo no es POST entonces
        form = TareaForm()

    contexto = {
        'proyecto': proyecto,
        'form': form
    }
    return render(request, 'agregar_tarea.html', contexto)



@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    filtro_estado = request.GET.get('filtro_estado', None)
    tareas = proyecto.tareas.all()
    if filtro_estado in ['todo', 'doing', 'done']:
        tareas = proyecto.tareas.filter( estado=filtro_estado)
        
    contexto = {
        'proyecto': proyecto,
        'tareas': tareas,
        'filtro_estado': filtro_estado
    }
    
    return render(request, 'detalle_proyecto.html', contexto)


@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        # Se envia el formulario con una instacia de la tarea que vamos a editar
        form = TareaForm(request.POST, request.FILES, instance=tarea)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.propietario = request.user
            tarea.save()
            return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)
    else:
        # Si el metodo no es POST
        form = TareaForm(instance=tarea)
    contexto = {
        'tarea': tarea,
        'form': form
    }
    return render(request, 'agregar_tarea.html', contexto)