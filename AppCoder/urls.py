from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.inicio,name='inicio'),
    #Mascota
    path('mascota',views.animal,name='mascota'),
    path('formularioMascota',views.formularioMascota,name='formularioMascota'),
    path('leerMascota',views.leerMascota,name='leerMascota'),
    path('eliminarMascota/<mascota_nombre>/',views.eliminarMascota,name='eliminarMascota'),
    path('editarMascota/<mascota_nombre>/',views.editarMascota,name='editarMascota'),
    path('busquedaMascota',views.busquedaMascota,name='busquedaMascota'),
    path('buscar/',views.buscar),
    #Persona
    path('persona',views.persona,name='persona'),
    path('formularioPersona',views.formularioPersona,name='formularioPersona'),
    path('leerPersona',views.leerPersona,name='leerPersona'), 
    path('eliminarPersona/<persona_nombre>/',views.eliminarPersona,name='eliminarPersona'),
    path('editarPersona/<persona_nombre>/',views.editarPersona,name='editarPersona'),

    #Vetirinario
    path('veterinario',views.veterinario,name='veterinario'),
    path('formularioVeterinario',views.formularioVeterinario,name='formularioVeterinario'),
    path('leerVeterinario',views.leerVeterinario,name='leerVeterinario'), 
    path('eliminarPersona/<persona_nombre>/',views.eliminarPersona,name='eliminarPersona'),
    path('editarPersona/<persona_nombre>/',views.editarPersona,name='editarPersona'),


    #Loguin/Register
    path('login',views.login_request, name='Login'),
    path('register',views.register, name='Register'),
    path('logout',LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
]