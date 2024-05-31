# API Gestion de Tareas Yuhu

Esta API te permite realizar operaciones CRUD en /tasks/ para generar tareas con un titulo, descripción, email (se usuara para asignar tareas y enviaran notificaciones), fecha de expiración (opcional), se meneja paginación en la obtención de tareas.

## Requisitos

- Python 3.12
- Postgresql
- Redis
- SO Linux

## Configuración del entorno virtual

1.**Clonar el Repositorio:**

> git clone https://github.com/StevenSanchezEs/api_gestion_tareas.git

2.**Acceder al Directorio del Proyecto:**

> cd gestion_tareas

3.**Crear y Activar el Entorno Virtual:**

> python3 -m venv venv

> source venv/bin/activate

4.**Instalar Dependencias:**

> pip install -r requirements.txt

5.**Crear archivo .env**
> vim .env

## Configuración de variables de entorno y Base de Datos

6.**Base de datos**

Debes tener una base de datos Postgres creada o crear una, para este ejemplo se creo una base de datos llamada **yuhu**, tu puedes elegir el de tu preferencia ya que en el archivo **.env** podras cambiar la configuración de tu base de datos si así lo requieres.


7.**Configurar variables de entorno para producción**

Los datos presentados a continuación son unicamente para representar un ejemplo, tienes que remplazar los valores por tus propias credenciales, el **SECRET KEY** es muy importante que lo cambies por uno propio generado por herramientas como **secrets** de Python, DEBUG debes cambiarlo a **False**, en **ALLOWED_HOST** y **CORS_ALLOWED_ORIGINS** por el dominio o ip donde se permitiran las solicitudes.

Ejemplo para definir Variables de entorno en el archivo .env creado previamente:
	
 	#Variables para Configuración Base de Datos
	POSTGRES_DB=gastion_tareas
	POSTGRES_USER=yuhu
	POSTGRES_PASSWORD=QnZXBYjwWpSkFcLOH
	POSTGRES_HOST=localhost
	POSTGRES_PORT=32076
	
	#Variables para Configuración de Correo SMTP
	EMAIL_HOST_SMTP=smtpout.ejemplo.net
	EMAIL_PORT_SMTP=587
	EMAIL_USE_TLS=True
	EMAIL_HOST_USER=tucorreo@dominio.com
	EMAIL_HOST_PASSWORD=TuC@ntraseñ@
	
	#Variables para Configuración de Server Redis
	REDIS_BROKER_URL=redis://:password@hostname:port/dbnumber
	REDIS_RESULT_BACKEND_URL=redis://:password@hostname:port/dbnumber
	
 	#Variables para configuracion de producción
	SECRET_KEY=d34hdbp&tde8_+zd2k)q$+u
	ALLOWED_HOSTS=api.yuhu.com
	CORS_ALLOWED_ORIGINS=api.yuhu.com
	DEBUG=False

Ejemplo secrets:
```python
import secrets

SECRET_KEY = secrets.token_urlsafe(32)
print(SECRET_KEY)
```

8.**Crear Migraciones y Migrar**

> python manage.py makemigrations

> python manage.py migrate

8.**Crear superuser**

Con este comando podras crear el superusuario el cual es necesario y te permitira consumir el endpoint /usuarios para crear más usuarios y asignar roles.
> python manage.py createsuperuser

## Deploy
Los siguientes datos son un ejemplo para deploy lo unico que se modifica conforme a las necesidades para el deploy es la **IP** o **Dominio** así como el **puerto** y **workers(-w)** estos datos se encuentran en el archivo llamado Procfile con el del ejemplo:

	web: gunicorn -w 4 -b 0.0.0.0:$PORT gestion_tareas.wsgi:application
	worker: celery -A gestion_tareas worker -l info
	beat: celery -A gestion_tareas beat -l info

Para ejecturar tanto el proyecto Django como Celery en paralelo usa el siguiente comando:

> honcho start

**Enspoints de la API**

Documentación de la API: 
/redoc/
/swagger/

GRUD Tasks: 
/api/tasks/

Generar Token:
/api/token/


**Notas**

Cada solicitud para consumir un endpoint requiere que se pase el token generado previamente en los Headers de la solicitud, por ejemplo:


Key: Authorization

Value: Token tutoken3242onoin23o4n32i3on34223oi