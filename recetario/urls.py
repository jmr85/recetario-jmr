
from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#     url(r'^$', 'recetario.views.home', name='home'),
#     url(r'^recetario/', include('recetario.foo.urls')),
     url(r'^$', 'principal.views.inicio', name='inicio'),
     url(r'^usuarios/$', 'principal.views.usuarios', name='usuarios'),
     url(r'^recetas/$', 'principal.views.lista_recetas', name='lista_recetas'),
     url(r'^receta/(?P<id_receta>\d+)$', 'principal.views.detalle_receta', name='detalle_receta'),
     url(r'^sobre/$', 'principal.views.sobre', name='sobre'),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT,}),
     url(r'^contacto/$', 'principal.views.contacto', name='contacto'),
     url(r'^receta/nueva/$', 'principal.views.nueva_receta', name='nueva_receta'),
     url(r'^comenta/$', 'principal.views.nuevo_comentario', name='nuevo_comentario'),
     url(r'^usuario/nuevo$', 'principal.views.nuevo_usuario', name='nuevo_usuario'),
     url(r'^ingresar/$', 'principal.views.ingresar', name='ingresar'),
     url(r'^privado/$', 'principal.views.privado', name='privado'),
     url(r'^cerrar/$', 'principal.views.cerrar', name='cerrar'),
)
