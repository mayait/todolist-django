from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='perfil', 
        help_text="Usuario al que pertenece este perfil")
    avatar = models.ImageField(
        upload_to='avatars/', 
        blank=True, 
        null=True, 
        help_text="Imagen de perfil")
    bio = models.TextField(
        blank=True, 
        null=True, 
        help_text="Breve biografia del usuario")
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
class Proyecto(models.Model):
    nombre = models.CharField(
        max_length=100, 
        help_text="Nombre del proyecto")
    descripcion = models.TextField(
        help_text="Descripcion del proyecto")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, 
        help_text="Fecha de creacion del proyecto")
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, 
        help_text="Fecha de ultima actualizacion del proyecto")
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADOS = [
        ('todo', 'Por hacer'),
        ('doing', 'En progreso'),
        ('done', 'Hecho'),
    ]
    proyecto = models.ForeignKey(
        Proyecto, 
        on_delete=models.CASCADE, 
        related_name='tareas', 
        help_text="Proyecto al que pertenece esta tarea")
    titulo = models.CharField(
        max_length=100, 
        help_text="Título de la tarea", verbose_name="Título")
    descripcion = models.TextField(
        null=True,
        blank=True,
        help_text="Descripcion de la tarea")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, 
        help_text="Fecha de creacion de la tarea")
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, 
        help_text="Fecha de ultima actualizacion de la tarea")
    estado = models.CharField(
        max_length=20, 
        default='todo', 
        choices = ESTADOS,
        help_text="Estado de la tarea")
    adjunto = models.FileField(
        upload_to='adjuntos/', 
        blank=True, 
        null=True, 
        help_text="Archivo adjunto")
    propietario = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE, 
        related_name='tareas', 
        help_text="Usuario propietario de la tarea")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-fecha_creacion']
    
    
    def class_color(self):
        if self.estado == 'todo':
            color = 'warning'
        elif self.estado == 'done':
            color = 'success'
        else:
            color = 'info'
        return color

    
    def __str__(self):
        return f"{self.titulo} ({self.get_estado_display()})"