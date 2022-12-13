from dataclasses import field
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AnimalFormulario(forms.Form):
    nombreAnimal= forms.CharField(max_length=40)
    edad= forms.IntegerField()
    tipo= forms.CharField(max_length=40)
    motivo= forms.CharField(max_length=40)
    fecha= forms.DateField()
    costo= forms.IntegerField()

class PersonaFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    telefono= forms.IntegerField()

class VeterinarioFormulario(forms.Form):
    veterinario = forms.CharField(max_length=20)
    apellidoVet = forms.CharField(max_length=40)
    matricula = forms.CharField(max_length=40)
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña Antigua', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña Antigua', widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}        