# Datos del grupo
## Integrantes
Raúl Alejandro Luna Vizcaíno
Joffre Steven Verdezoto Tejena
## Carrera
Ingeniería Informatica
## Materia
Desarrollo de aplicaciones web
## Proyecto
Películas y directores: Cine Mundo
## Fecha de entrega 
3 de febrero de 2025

# Proyecto Final: Peliculas y directores (Django)
El presente proyecto consiste en el trabajo final de la materia de desarrollo de aplicaciones web, con la finalidad
de demostrar los conocimientos adquiridos durante el curso de la materia. De esta forma se establece la parte del backend
con **Django**, utilizando el patrón Modelo - Vista - Controlador (MVC).

# Objetivos 
- Reforzar conocimientos adquiridos durante el transcurso de la materia.
- Comprender y aplicar la creación de una api en Django.
- Implementar relaciones entre modelos (Director → Películas).
- Desarrollar una aplicación web funcional y navegable. 

# Descripción del proyecto
La aplicación funcionara como una cartelera de peliculas dentro de la cual se podra observar una sección de peliculas y una seccion de directores, con los respectivos parametros a observar en cada una de las secciones.

# Requisitos

- Python 3.10 o superior
- Django
- Entorno virtual (recomendado)

# Instalación y configuración
### Instalación de gestor de ambientes virtuales de python
sudo apt install python3-venv
### Creación del entorno virtual
python -m venv .venv
### Activación del entorno virtual
.venv\Scripts\activate
### Instalación de dependendencias
pip install -r requirements.txt
### Desactivar el ambiente
deactivate

# Comandos a utilizar
### Ejecución del servidor
python manage.py runserver
### Creación super usuario
python manage.py createsuperuser
### Crear archivos de migraciones
python manage.py makemigrations
### Migrar a base de datos
python manage.py migrate
### Almacenamiento de nuevas dependencias
pip freeze > requirements.txt
