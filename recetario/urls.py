
from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#     url(r'^$', 'recetario.views.home', name='home'),
#     url(r'^recetario/', include('recetario.foo.urls')),
     url(r'^$', 'principal.views.inicio'),
     url(r'^usuarios/$', 'principal.views.usuarios'),
     url(r'^recetas/$', 'principal.views.lista_recetas'),
     url(r'^receta/(?P<id_receta>\d+)$', 'principal.views.detalle_receta', name='detalle_receta'),
     url(r'^sobre/$', 'principal.views.sobre'),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT,}),
     url(r'^contacto/$', 'principal.views.contacto'),
     url(r'^receta/nueva/$', 'principal.views.nueva_receta'),
     url(r'^comenta/$', 'principal.views.nuevo_comentario'),
     url(r'^usuario/nuevo$', 'principal.views.nuevo_usuario'),
     url(r'^ingresar/$', 'principal.views.ingresar'),
     url(r'^privado/$', 'principal.views.privado'),
     url(r'^cerrar/$', 'principal.views.cerrar'),
)
