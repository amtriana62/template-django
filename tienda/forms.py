#para crear el formulario dinamico-paso edicion
from django import forms
from .models import Hoja #incluir el modelo

class HojaForm(forms.ModelForm):
    class Meta:
        model=Hoja
        fields='__all__' #el mapeado del formulario