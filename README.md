# Web Personal

## *Curso Práctico de Django con Python: Desarrollo Web Backend*

**Web Personal** es un proyecto básico de introducción al framework *Django*, basado en la creación de una web sencilla con un portafolio dinámico y un panel de administrador para manejar los proyectos del portafolio.

Incluye:
+ **Django REST Framework**
+ **Django Templates**
+ Entorno virtual con **Pipenv**
+ Personalización del panel administrador de _Django_

### Librerías y paquetes utilizados:
- [**Django REST framework**](https://www.django-rest-framework.org/#installation)

### Versión: 1.0.0

### Notas:
Comando para activar el entorno virtual:
```
pipenv shell
```

Comando para ver todos los paquetes (con sus dependencias) instaladas:
```
pip list --local
```
o
```
pipenv graph
```

Comando para instalar las dependencias del proyecto desde el fichero requirements.txt (con el entorno virtual activado):
```
pip install -r requirements.txt
```

Comando para crear o actualizar el fichero requirements.txt (con el entorno virtual activado):
```
pip freeze > requirements.txt
```

Comando para ejecutar el servidor en desarrollo:
```
python manage.py runserver
```