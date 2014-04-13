# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Receta(models.Model):     
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField()
    preparacion = models.TextField()
    imagen = models.ImageField(upload_to='recetas', verbose_name=_('Imagen'))
    tiempo_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name=_('receta')
        verbose_name_plural=_('recetas')
    
    def __unicode__(self):
        return self.titulo
        
class Comentario(models.Model):        
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text=_('Tu comentario'), verbose_name=_('Comentario'))

    class Meta:
        verbose_name=_('comentario')
        verbose_name_plural=_('comentarios')
    
    def __unicode__(self):
        return self.texto
    
    
