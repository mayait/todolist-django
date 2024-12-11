from django import forms
from .models import Proyecto, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto # Referencia al Proecto de models.py
        fields = ['nombre', 'descripcion']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea # Referencia a la Tarea de models.py
        fields = [
            #'proyecto', 
            'titulo', 
            'descripcion', 
            'estado', 
            'adjunto', 
            ]
        
# Formset para tareas nos permite tener instancias de un hijo en un formulario padre

TareaFormSet = forms.inlineformset_factory(
    Proyecto, # Padre
    Tarea, # Hijo
    form=TareaForm, # formulario hijo,
    extra=5, # cantidad de formularios hijos
    can_delete=True, # si se pueden eliminar los formularios hijos
    )
