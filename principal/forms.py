# -*- coding: utf-8 -*-
from django import forms
from principal.models import Receta, Comentario
from django.forms import ModelForm

class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tu correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea)

class RecetaForm(ModelForm):
    class Meta:
        model = Receta

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
    
