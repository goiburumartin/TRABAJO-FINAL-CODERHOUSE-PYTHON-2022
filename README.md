# Proyecto Final del curso de Python CoderHouse realizado por Martin Goiburu y Martin Torres.
El proyecto trata de una app web sobre una Veterinaria, la cual se puede cargar, visualizar, editar y eliminar los datos de la mascota, el dueño y el veterinario.

# Video demostrativo
Adjunto a continuacion un link de Drive donde se encuentra cargado un video demostrando el funcionamiento de la pagina web.

https://drive.google.com/drive/folders/17KwUDSPAefmFuwCCZb7KIF-NZcrtQ_bl?usp=share_link
_______________________________________________________________________________________________________________________________________________________________________
# Models.py:
Aca encontraremos lo siguiente:

*modelo Animal.
-nombreAnimal(Char, nombre de la mascota)
-edad(Integer,edad de la mascota)
-tipo(Char,ej:perro,gato,loro,etc)
-motivo(Char,ej:peluqueria,vacunas,etc)
-fecha(Date,es la fecha de ingreso)
-costo(Integer, el precio de lo que lo se le haya hecho al animal)

*modelo Persona. 
-nombre(Char, nombre del dueño)
-apellido= (Char, apellido del dueño)
-telefono= (Integer, numero del dueño)

*modelo Veterinario. 
-veterinario(Char, nombre)
-apellidoVet= (Char, apellido)
-matricula= (Integer, numero de matricula)
_______________________________________________________________________________________________________________________________________________________________________
# Forms.py:
En este archivo podemos encontrar los formularios usados para cargar los datos que quedan guardados en nuestra base de datos.
Son 5 los formularios, uno por cada modelo , otro para poder registrar los usuarios nuevos y el último que sirve para edirtar el perfil de un usuario.
_______________________________________________________________________________________________________________________________________________________________________
# Urls.py:
Contiene todas las rutas de la web. 
_______________________________________________________________________________________________________________________________________________________________________
# Views.py:
Aparecen todas las vistas que se utilizan en la app.
Asociado a lo anterior por cada modelo se aplica el concepto de CRUD(Create, Read, Update, Delete); una vista de logueo, registro y edicion de perfil del usuario. Además tenemos la vista para buscar una mascota por su nombre.
Ejemplo de vistas (CRUD) para el Modelo Animal:

Create: vista formularioMascota

Read: vista leerMascota

Update: vista editarMascota

Delete: vista eliminarMascota

_______________________________________________________________________________________________________________________________________________________________________
# Templates:
Es una carpeta donde se encuentran todos los archivos HTML. Se utilza una platilla de BOOSTRAP y se aplica el concep de herencia a cada archivo.

_______________________________________________________________________________________________________________________________________________________________________
# comision: 34635
# Profesor: Ochoa Daniel
# Tutor: Herrera Jhonathan
# Integrantes del trabajo: Torres Martin y Goiburu Martin
