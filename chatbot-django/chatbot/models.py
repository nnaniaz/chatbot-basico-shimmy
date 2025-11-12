from django.db import models
from django.contrib.auth.models import User

class Conversacion(models.Model):
    pregunta = models.TextField()
    respuesta = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    temperatura = models.FloatField(default=0.8)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50, default='gemma3:1b')

    def __str__(self):
        return f"{self.pregunta} - {self.usuario.username}"
    
    class Meta:
        verbose_name_plural = "Conversación"
        verbose_name = "Conversaciones"


class Documento(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    metadatos = models.JSONField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Documentos"
        verbose_name = "Documentos"