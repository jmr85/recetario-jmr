'''
Created on 09/01/2013

@author: juan.martin.ruiz@gmail.com
'''
"""este modulo no vino con la instalacion de django, registra 
el modelo Receta y Comentario en admin"""

from principal.models import Receta, Comentario
from django.contrib import admin

admin.site.register(Receta)
admin.site.register(Comentario)


