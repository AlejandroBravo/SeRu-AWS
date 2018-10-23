from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User


class Formulario_Registro(UserCreationForm):
    telofono_contacto = forms.CharField(max_length=9, help_text='Introduce tu numero de movil')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('telofono_contacto',)