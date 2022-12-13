from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import AnimalFormulario,PersonaFormulario,UserRegisterForm,VeterinarioFormulario,UserEditForm
from AppCoder.models import Animal, Avatar,Persona,Veterinario
#CVB
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
#-Loguin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

 
# Create your views here.


#-----------------------------------------Mascota-------------------------------------------------------
def animal(request):
    return render(request,"AppCoder/animal.html")

@login_required
def leerMascota(request):
    mascotas = Animal.objects.all()
    contexto = {"mascotas":mascotas}
    return render(request,"AppCoder/animal.html",contexto)

def formularioMascota(request):
    if request.method == 'POST':
        miFormulario = AnimalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
		    
            mascota = Animal(nombreAnimal=informacion['nombreAnimal'],
            edad=informacion['edad'],tipo=informacion['tipo'],
            motivo=informacion['motivo'],fecha=informacion['fecha'],
            costo=informacion['costo'])
		    
            mascota.save()

            mascotas = Animal.objects.all()
    
            return render(request,"AppCoder/animal.html",{"mascotas":mascotas})

    else:
        miFormulario = AnimalFormulario()
    return render(request, "AppCoder/formularioMascota.html",{"miFormulario":miFormulario})

def editarMascota(request,mascota_nombre):

    mascota = Animal.objects.get(nombreAnimal = mascota_nombre)

    if request.method == 'POST':
        miFormularioMascota = AnimalFormulario(request.POST)
        print(miFormularioMascota)

        if miFormularioMascota.is_valid:
            
            informacion = miFormularioMascota.cleaned_data
		    
            mascota.nombreAnimal=informacion['nombreAnimal']
            mascota.edad=informacion['edad']
            mascota.tipo=informacion['tipo']
            mascota.motivo=informacion['motivo']
            mascota.fecha=informacion['fecha']
            mascota.costo=informacion['costo']
		    
            mascota.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioMascota= AnimalFormulario(initial={'nombreAnimal': mascota.nombreAnimal, 'edad': mascota.edad , 
            'tipo': mascota.tipo, 'motivo':mascota.motivo ,'fecha':mascota.fecha , 'costo':mascota.costo }) 
    
    return render(request, "AppCoder/editarMascota.html", {"miFormularioMascota": miFormularioMascota, "mascota_nombre":mascota_nombre})
        
def eliminarMascota(request,mascota_nombre):
    mascota = Animal.objects.get(nombreAnimal=mascota_nombre)
    mascota.delete()
    mascotas = Animal.objects.all()
    contexto ={"mascotas":mascotas}
    return render(request,"AppCoder/animal.html",contexto)

@login_required
def busquedaMascota(request):
    return render(request,"AppCoder/busquedaMascota.html")
    
@login_required
def buscar(request):
        
    if request.GET["nombreAnimal"]:
        nombreAnimal = request.GET['nombreAnimal']
        mascotas = Animal.objects.filter(nombreAnimal__icontains=nombreAnimal)
        
        return render(request, "AppCoder/animal.html",{"mascotas":mascotas})

    else:
        respuesta = "No enviaste nada"
    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})


#-----------------------------------------Persona-------------------------------------------------------
def persona(request):
    return render(request,"AppCoder/persona.html")

@login_required
def leerPersona(request):
    personas = Persona.objects.all()
    contexto = {"personas":personas}
    return render(request,"AppCoder/persona.html",contexto)

def formularioPersona(request):

    if request.method == 'POST':
        miFormularioPersona = PersonaFormulario(request.POST)
        print(miFormularioPersona)

        if miFormularioPersona.is_valid:
            
            informacion = miFormularioPersona.cleaned_data
		    
            persona = Persona(nombre=informacion['nombre'],
            apellido=informacion['apellido'],telefono=informacion['telefono'])
		    
            persona.save()

            personas = Persona.objects.all()
            
            return render(request,"AppCoder/persona.html",{"personas":personas})

    else:
        miFormularioPersona = PersonaFormulario()
    return render(request, "AppCoder/formularioPersona.html",{"miFormularioPersona":miFormularioPersona})

def editarPersona(request,persona_nombre):

    persona = Persona.objects.get(nombre = persona_nombre)

    if request.method == 'POST':
        miFormularioPersona = PersonaFormulario(request.POST)
        print(miFormularioPersona)

        if miFormularioPersona.is_valid:
            
            informacion = miFormularioPersona.cleaned_data
		    
            persona.nombre=informacion['nombre']
            persona.apellido=informacion['apellido']
            persona.telefono=informacion['telefono']
		    
            persona.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioPersona= PersonaFormulario(initial={'nombre': persona.nombre, 'apellido':persona.apellido , 
            'telefono':persona.telefono}) 
    
    return render(request, "AppCoder/editarPersona.html", {"miFormularioPersona": miFormularioPersona, "persona_nombre":persona_nombre})
        
def eliminarPersona(request,persona_nombre):
    persona = Persona.objects.get(nombre=persona_nombre)
    persona.delete()
    personas = Persona.objects.all()
    contexto ={"personas":personas}
    return render(request,"AppCoder/persona.html",contexto)


#Veterinario
def veterinario(request):
    return render(request,"AppCoder/veterinario.html")

@login_required
def leerVeterinario(request):
    veterinarios = Veterinario.objects.all()
    contexto = {"veterinarios":veterinarios}
    return render(request,"AppCoder/veterinario.html",contexto)

def formularioVeterinario(request):

    if request.method == 'POST':
        miFormularioVeterinario = VeterinarioFormulario(request.POST)
        print(miFormularioVeterinario)

        if miFormularioVeterinario.is_valid:
            
            informacion = miFormularioVeterinario.cleaned_data
		    
            veterinario = Veterinario(veterinario=informacion['veterinario'],
            apellidoVet=informacion['apellidoVet'],matricula=informacion['matricula'])
		    
            veterinario.save()

            veterinarios = Veterinario.objects.all()
            
            contexto = {"veterinarios":veterinarios}
            return render(request,"AppCoder/veterinario.html",contexto)

    else:
        miFormularioVeterinario = VeterinarioFormulario()
    return render(request, "AppCoder/formularioVeterinario.html",{"miFormularioVeterinario":miFormularioVeterinario})




#Loguin/Register
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario,password = contra)

            if user is not None:
                login(request,user)

                return render(request,"AppCoder/inicio.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                
                return render(request,"AppCoder/inicio.html",{"mensaje":"Error,datos incorrectos"})

        else:
            
                return render(request,"AppCoder/inicio.html",{"mensaje":"Error,formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"AppCoder/login.html",{'form':form})


def register(request):
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html",{"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()
        
    return render(request,"AppCoder/registro.html",{"form":form})


def inicio(request):
    return render(request,"AppCoder/inicio.html")

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password1']            
            usuario.save()
            

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "AppCoder/editarPerfil.html",{"miFormulario": miFormulario, "usuario":usuario})



#Avatar
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,"AppCoder/inicio.html", {"url":avatares[0].imagen.url})
