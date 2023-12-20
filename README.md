# Challenge EGO

Esta aplicación se ha desarrollado utilizando Django como parte de la prueba técnica para la posición de Desarrollador Backend Python/Django en la empresa EGO. El objetivo principal ha sido la creación del backend y una API para una aplicación específica.

## Aviso

Todos los comandos para la instalación y uso del proyecto estan destinados a usuarios de Windows, si estas utilizando Linux o MacOS es posible que halla variaciones.

### Requisitos previos

- Python 3.11

### Instalación

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/MartinFernandezSantia/EGO_Test_dev.git
   ```

2. **Instalar Dependencias:**

   ```bash
   cd EGO_Test_dev
   pip install -r requirements.txt
   ```

### Uso

- Iniciar el proyecto en localhost puerto 8000.

  ```bash
  python manage.py runserver
  ```

- Crear un superusuario para poder acceder al panel de administración:

  ```bash
  python manage.py createsuperuser
  ```

- URLs

  - **localhost:8000/admin** *#Panel de administración*
  - **localhost:8000/api/vehiculos** *#Json de todos los vehiculos*
  - **localhost:8000/api/vehiculos/{id}** *#Json de un vehiculo*
  - **localhost:8000/api/modelos_vehiculos** *#Json de todos los modelos de vehiculos*
  - **localhost:8000/api/modelos_vehiculos/{id}** *#Json de un modelo de vehiculo*
  - **localhost:8000/api/imagenes** *#Json de todas las imagenes*
  - **localhost:8000/api/imagenes/{id}** *#Json de una imagen*
  - **localhost:8000/api/colores** *#Json de todos los colores*
  - **localhost:8000/api/colores/{id}** *#Json de uno de los colores*
