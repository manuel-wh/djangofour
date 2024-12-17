# djangocuatro# Manual para iniciar un proyecto de Django

# Estructura del proyecto

Elaborado con Django 3.2.12 y Python 3.6

Para iniciar un proyecto siga las siguientes instrucciónes



1. **Adaptar este [manual](https://github.com/desarrollowh/django_base/blob/master/docs/installation.md) con el nombre de tu proyecto.**
   
   Copiamos todo este archivo en una carpeta temporal.

   Reemplazamos todo lo que diga `djangocuatro` por el nombre de tu proyecto.

   Ejemplo:
   ![image](https://user-images.githubusercontent.com/85954707/156051961-e5dd88c9-d0aa-41a6-b365-47ed150a4bfb.png)


   ---





2. **Definir la ubicación del directorio del proyecto y su nombre**

   Abrimos una terminal que nos ayudara durante todo el proceso. Utilice siempre esta terminal donde se definiran las variables de la ruta a su proyecto.

   2.1 Posicionate en el siguiente directorio

   ```bash
   cd ~/Documentos
   ```

   2.2 En la terminal copia y pegue las siguientes variables para definirlas y que nos ayuden en las siguientes instrucciones

    ```bash
   export PROJECT_NAME="djangocuatro"
   export PROJECT_DIR=$(pwd)/$PROJECT_NAME
    ```

   ---





3. **Crear un entorno virtual de pruebas solo para usar el comando `django-admin`**

   3.1 Crea un entorno virtual de pruebas solo utilizar el comando `django-admin`
   > Debes tener configurado la variable WORKON_HOME en tu `~/.bashrc`
   
![image](https://user-images.githubusercontent.com/85954707/156048076-c4003458-22a2-42af-8127-b5911b6bd01c.png)

   ```bash
   mkvirtualenv djangoadmin --python 3.6
   ```
   NOTA: Si tienes un error como: _"The path 3.6 (from --python=3.6) does not exist"_ al intentar crear el entorno. Puedes probar con estos las siguientes dos alternativas:
   
   Opcion 1:
   ```bash
   mkvirtualenv djangoadmin -p python3.6
   ```
   Opcion 2:
   ```bash
   cd $WORKON_HOME
   virtualenv -p python3 djangoadmin
   workon djangoadmin
   cd ~/Documentos
   ```
   3.2 Instala django en su version 3.2.12

   ```bash
   pip install django==3.2.12
   ```

   ---




4. **Inicia un proyecto de Django con `django-admin`**

   4.1 Crea un proyecto de django

   ```bash
   django-admin startproject $PROJECT_NAME
   ```

   4.2 Entra a la carpeta del proyecto

   ```bash
   cd $PROJECT_DIR
   ```

   4.3 Desactiva del entorno virtual de pruebas creado anteriormente

   ```bash
   deactivate
   ```

   ---





5. **Crea el entorno real del proyecto con `pipenv`**

   5.1 Crea el entorno virtual y genera el Pipfile

   ```bash
   pipenv shell --python 3.6
   ```

   5.2 Instala los paquetes iniciales del proyecto (`django` y `django-environ`)

   ```bash
   pipenv install django==3.2.12 django-environ==0.8.1
   ```

   ---





6. **Mover las variables sensibles `DEBUG` y `SECRET_KEY` del settings en un archivo .env**

   6.1 Con los siguientes comandos crearemos la carpeta para almacenar los environments de desarrollo *(development)* y producción *(production)*.

   ```bash
   # Carpeta contendora .config/environment
   mkdir $PROJECT_DIR/.config
   mkdir $PROJECT_DIR/.config/environment
   # Archivos .envs de desarrollo
   mkdir $PROJECT_DIR/.config/environment/development
   touch $PROJECT_DIR/.config/environment/development/.env
   touch $PROJECT_DIR/.config/environment/development/.env_example
   # Archivos .envs de producción
   mkdir $PROJECT_DIR/.config/environment/production
   touch $PROJECT_DIR/.config/environment/production/.gitkeep
   ```

   

   6.2 Editar el archivo `.config/environment/development/.env_example` para poner poner lo siguiente.

   ```bash
   nano $PROJECT_DIR/.config/environment/development/.env_example
   ```

   ```
   DEBUG=
   SECRET_KEY=
   ```

   

   6.3 Edite el archivo `.config/environment/development/.env` y copie el valor de la variable  `SECRET_KEY` que django pone por defecto en el archivo `settings.py` linea #23

   ```bash
   nano $PROJECT_DIR/.config/environment/development/.env
   ```

   ```
   DEBUG=1
   SECRET_KEY=django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

   

   6.4 En el archivo `settings.py` **remplace desde la linea 13 a la linea 26** por lo siguiente.

   ```bash
   nano $PROJECT_DIR/$PROJECT_NAME/settings.py
   ```

   ```python
   import os
   from pathlib import Path
   import environ
   
   
   # Build paths inside the project like this: BASE_DIR / 'subdir'.
   BASE_DIR = Path(__file__).resolve().parent.parent
   
   # Get the djangocuatro_ENVIRON value to load the env variables
   server_env = os.environ.get('djangocuatro_ENVIRON') or 'development'
   path = str(BASE_DIR / F'.config/environment/{server_env}/.env')
   environ.Env.read_env(path)
   
   env = environ.Env(
       # set casting, default value
       DEBUG=(bool, True),
       SECRET_KEY=(str, ),
   )
   
   # Quick-start development settings - unsuitable for production
   # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
   
   # SECURITY WARNING: keep the secret key used in production secret!
   SECRET_KEY = env('SECRET_KEY')
   
   # SECURITY WARNING: don't run with debug turned on in production!
   DEBUG = env('DEBUG')
   ```

   

   6.5 En la instrucción del settings `server_env = os.environ.get('djangocuatro_ENVIRON') or 'development'`, cambie su `djangocuatro_ENVIRON` para que todo quede en mayusculas.
   ![image](https://user-images.githubusercontent.com/85954707/156002442-4311c68c-5a6e-423a-bfad-6ffa2820b39f.png)


   6.6 **Corra el proyecto de Django para verificar que los cambios anteriores se han efectuado correctamente. Hasta este punto se esta utilizando las variables de entorno.**
   ```bash
   cd $PROJECT_DIR
   python manage.py runserver
   ```

---



7. **Comenzar a trackear los cambios con el controlador de versión Git**

   7.1 Debe crear el archivo `.gitignore` y agregar lo siguiente

   ```bash
   nano $PROJECT_DIR/.gitignore
   ```

   ```
   # Byte-compiled / optimized / DLL files
   __pycache__/
   *.py[cod]
   *$py.class
   
   # C extensions
   *.so
   
   # Distribution / packaging
   .Python
   build/
   develop-eggs/
   dist/
   downloads/
   eggs/
   .eggs/
   lib/
   lib64/
   parts/
   sdist/
   var/
   wheels/
   share/python-wheels/
   *.egg-info/
   .installed.cfg
   *.egg
   MANIFEST
   
   # PyInstaller
   #  Usually these files are written by a python script from a template
   #  before PyInstaller builds the exe, so as to inject date/other infos into it.
   *.manifest
   *.spec
   
   # Installer logs
   pip-log.txt
   pip-delete-this-directory.txt
   
   # Unit test / coverage reports
   htmlcov/
   .tox/
   .nox/
   .coverage
   .coverage.*
   .cache
   nosetests.xml
   coverage.xml
   *.cover
   *.py,cover
   .hypothesis/
   .pytest_cache/
   cover/
   
   # Translations
   *.mo
   *.pot
   
   # Django stuff:
   *.log
   local_settings.py
   db.sqlite3
   db.sqlite3-journal
   
   # Flask stuff:
   instance/
   .webassets-cache
   
   # Scrapy stuff:
   .scrapy
   
   # Sphinx documentation
   docs/_build/
   
   # PyBuilder
   .pybuilder/
   target/
   
   # Jupyter Notebook
   .ipynb_checkpoints
   
   # IPython
   profile_default/
   ipython_config.py
   
   # pyenv
   #   For a library or package, you might want to ignore these files since the code is
   #   intended to run in multiple environments; otherwise, check them in:
   # .python-version
   
   # pipenv
   #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
   #   However, in case of collaboration, if having platform-specific dependencies or dependencies
   #   having no cross-platform support, pipenv may install dependencies that don't work, or not
   #   install all needed dependencies.
   #Pipfile.lock
   
   # poetry
   #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
   #   This is especially recommended for binary packages to ensure reproducibility, and is more
   #   commonly ignored for libraries.
   #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
   #poetry.lock
   
   # PEP 582; used by e.g. github.com/David-OConnor/pyflow
   __pypackages__/
   
   # Celery stuff
   celerybeat-schedule
   celerybeat.pid
   
   # SageMath parsed files
   *.sage.py
   
   # Environments
   .env
   .venv
   env/
   venv/
   ENV/
   env.bak/
   venv.bak/
   
   # Spyder project settings
   .spyderproject
   .spyproject
   
   # Rope project settings
   .ropeproject
   
   # mkdocs documentation
   /site
   
   # mypy
   .mypy_cache/
   .dmypy.json
   dmypy.json
   
   # Pyre type checker
   .pyre/
   
   # pytype static type analyzer
   .pytype/
   
   # Cython debug symbols
   cython_debug/
   
   # PyCharm
   #  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
   #  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
   #  and can be added to the global gitignore or merged into this file.  For a more nuclear
   #  option (not recommended) you can uncomment the following to ignore the entire idea folder.
   .idea/
   
   
   # Ignore all .env files for development and production
   .config/environment/development/*
   !.config/environment/development/.env_example
   .config/environment/production/*
   !.config/environment/production/.gitkeep
   
   # Ignore settings_server.py. Because it's for local purpose
   djangocuatro/settings_server.py
   
   # Ignore all developer's notes
   .notes/*
   !.notes/.gitkeep
   
   # Ignore collectstatic's directories
   media/*
   !media/.gitkeep
   static/*
   !static/.gitkeep
   
   # Ignore all media files
   djangocuatro/media/*
   !djangocuatro/media/.gitkeep
   
   ```

   7.2 Inicie el repositorio de git y agregemos todos los cambios de ahora al controlador de versiones con.

   ```bash
   cd $PROJECT_DIR
   
   git init
   git add .
   git commit -m "Inicio proyecto djangocuatro"
   ```

   7.3 (OPCIONAL) Puedes subir tu primer commit a algun repositorio si lo deseas agregando su remote y dando push.
   
   ```bash  
   git remote add origin <your-respoitory-url>
   git push origin <your-main-branch-name>
   ```

   ---






8. **Crear el directorio `core`**

   8.1 Crear el directorio como un modulo de python.

   ```bash
   mkdir $PROJECT_DIR/$PROJECT_NAME/core
   touch $PROJECT_DIR/$PROJECT_NAME/core/__init__.py
   ```

   8.2 Mover los archivos `urls.py`, `wsgi.py` y `asgi.py` al directorio `core/`

   ```bash
   mv $PROJECT_DIR/$PROJECT_NAME/urls.py $PROJECT_DIR/$PROJECT_NAME/core
   mv $PROJECT_DIR/$PROJECT_NAME/wsgi.py $PROJECT_DIR/$PROJECT_NAME/core
   mv $PROJECT_DIR/$PROJECT_NAME/asgi.py $PROJECT_DIR/$PROJECT_NAME/core
   ```

   8.3 Actualizar el archivo `settings.py` para decirle a Django donde puede encontrar los archivos que movimos.

   ```bash
   nano $PROJECT_DIR/$PROJECT_NAME/settings.py
   ```

   8.3.1 Busca la variable `ROOT_URLCONF` y reemplaza su valor por lo siguiente.

   ```python
   ROOT_URLCONF = 'djangocuatro.core.urls'
   ```

   8.3.2 Busca la variable `WSGI_APPLICATION` y reemplaza su valor por lo siguiente.

   ```python
   WSGI_APPLICATION = 'djangocuatro.core.wsgi.application'
   ```

---


9. **Crear el directorio `docs`**

   ```bash
   mkdir $PROJECT_DIR/docs
   touch $PROJECT_DIR/docs/README.md
   ```

---


10. **Crear el directorio `.logs`**

    ```bash
    mkdir $PROJECT_DIR/.logs
    touch $PROJECT_DIR/.logs/.gitkeep
    ```

---


11. **Crear el directorio `.notes`**

    ```bash
    mkdir $PROJECT_DIR/.notes
    touch $PROJECT_DIR/.notes/README.md
    ```

---


12. **Crear el directorio `.deployment`**

    ```bash
    mkdir $PROJECT_DIR/.deployment
    mkdir $PROJECT_DIR/.deployment/scripts
    touch $PROJECT_DIR/.deployment/scripts/.gitkeep
    ```

---


13. **Crear el directorio `.config/ssl_certs`**

    ```bash
    mkdir $PROJECT_DIR/.config/ssl_certs
    touch $PROJECT_DIR/.config/ssl_certs/.gitkeep
    ```

---


14. **Crear el directorio `static`, `media` y `locale`**

    14.1 Crear los archivos y directorios

    ```bash
    # locale
    mkdir $PROJECT_DIR/locale
    touch $PROJECT_DIR/locale/.gitkeep
    
    # media
    mkdir $PROJECT_DIR/media
    touch $PROJECT_DIR/media/.gitkeep
    mkdir $PROJECT_DIR/$PROJECT_NAME/media
    touch $PROJECT_DIR/$PROJECT_NAME/media/.gitkeep
    
    # static
    mkdir $PROJECT_DIR/static
    touch $PROJECT_DIR/static/.gitkeep
    mkdir $PROJECT_DIR/$PROJECT_NAME/static
    mkdir $PROJECT_DIR/$PROJECT_NAME/static/css
    touch $PROJECT_DIR/$PROJECT_NAME/static/css/styles.css
    mkdir $PROJECT_DIR/$PROJECT_NAME/static/js
    touch $PROJECT_DIR/$PROJECT_NAME/static/js/index.js
    mkdir $PROJECT_DIR/$PROJECT_NAME/static/fonts
    touch $PROJECT_DIR/$PROJECT_NAME/static/fonts/.gitkeep
    mkdir $PROJECT_DIR/$PROJECT_NAME/static/images
    touch $PROJECT_DIR/$PROJECT_NAME/static/images/.gitkeep
    ```

    14.2 Modificar el archivo settings para especificar la ruta de los directorios

       ```bash
    nano $PROJECT_DIR/$PROJECT_NAME/settings.py
       ```

    14.2.1 Agrega la variable `LOCALE_PATHS` con el siguiente valor.

    ```python
    LOCALE_PATHS = [
        BASE_DIR / 'locale',
    ]
    ```

    14.2.2 Asegurate de que exista la variable `STATIC_URL` y este definida con lo siguiente.

    ```python
    STATIC_URL = '/static/'
    ```

    14.2.3 Agrega la variable `STATICFILES_DIRS` con el siguiente valor.

    ```python
    STATICFILES_DIRS = [
        BASE_DIR / 'djangocuatro/static',
    ]
    ```


---


15. **Crear la app _"users"_ en `apps/users`**

    15.1 Cree el directorio `apps` destinada a almacenar todas las aplicaciones de nuestro proyecto

    ```bash
    mkdir $PROJECT_DIR/$PROJECT_NAME/apps
    ```

    15.2 Cree una nueva app llamada _"users"_ con el `django-admin`

    ```bash
    cd $PROJECT_DIR/$PROJECT_NAME/apps
    django-admin startapp users
    cd $PROJECT_DIR
    ```

---


16. **Crear el modelo custom _"User"_ heredando de `AbstractUser`**

    16.1 Creamos nuestro modelo custom "User" por recomendación de la documentación de Django.

    ```bash
    nano $PROJECT_DIR/$PROJECT_NAME/apps/users/models.py
    ```

    Reemplaza todo el contenido de `apps/users/models.py` por lo siguiente

    ```python
    from django.contrib.auth.models import AbstractUser
    
    
    # Create your models here.
    class User(AbstractUser):
        pass
    ```

    

    16.2 Registrar este nuevo modelo en el admin

    ```bash
    nano $PROJECT_DIR/$PROJECT_NAME/apps/users/admin.py
    ```

    Reemplaza todo el contenido de `apps/users/admin.py` por lo siguiente. **Aseguranse que la importación de los paquetes en local este bien**.

    ```python
    # django packages
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    # local packages
    from djangocuatro.apps.users.models import User
    
    
    # Register your models here.
    admin.site.register(User, UserAdmin)
    
    ```

    16.3 Modificar el _"name"_ de nuestra app en el archivo `apps/users/apps.py`

    ```bash
    nano $PROJECT_DIR/$PROJECT_NAME/apps/users/apps.py
    ```

    Reemplaza todo el contenido de `apps/users/apps.py` por lo siguiente. **Asegurandote que se haga referencia al nombre de su proyecto en la variable "name"**.

    ```python
    from django.apps import AppConfig
    
    
    class UsersConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'djangocuatro.apps.users'
    ```

    16.4 Modifique el archivo `settings.py` para terminar la configuración del modelo custom de __*"User"*__. 

    ```bash
    nano $PROJECT_DIR/$PROJECT_NAME/settings.py
    ```

    16.4.1 Agrege la nueva app `users`

    Busque la variable `INSTALLED_APPS` y agrege la nueva app que creamos

    ```python
    INSTALLED_APPS = [
        # ...
        'djangocuatro.apps.users',
    ]
    ```

    16.4.2 Agregar la variable `AUTH_USER_MODEL` para designar este nuevo modelo personalizado de _"User"_

    ```python
    AUTH_USER_MODEL = 'users.User'
    ```

    16.4.3 Realize la migración del nuevo modelo y aplique la migración en base de datos

    ```bash
    cd $PROJECT_DIR
    python manage.py makemigrations
    python manage.py migrate
    ```
    ---

17. __Try import `settings_server.py`__

    17.1 Crear el archivo `settings_server.py`. Este archivo esta destinado unicamente para pruebas en local y debe usarse como ultimo recurso.

    ```bash
    touch $PROJECT_DIR/$PROJECT_NAME/settings_server.py
    ```

    17.2 Agrege __al final del archivo__ `settings.py` el try/except del import

    ```bash
    nano $PROJECT_DIR/$PROJECT_NAME/settings.py
    ```
    ```python
    # Keep this at the end of the file.
    # Use this section as the last resort. Try to fix everything 
    # with django-environ package
    try:
        # Try import settings_server.py for local purpose.
        from settings_server import *
    except ImportError:
        # Doesn't matter if settings_server.py not exist.
        pass
    ```

18.__Ejecute el proyecto para ver que los cambios se realizaran correctamente__
   ```bash
   cd $PROJECT_DIR
   python manage.py runserver
   ```

19. __(OPCIONAL) Crear el directorio `apps/<app_name>/api`__

    19.1 Si se tiene una implementación con Django Rest Framework crear el siguiente directorio

    ```bash
    mkdir $PROJECT_DIR/$PROJECT_NAME/apps/users/api
    touch $PROJECT_DIR/$PROJECT_NAME/apps/users/api/__init__.py
    touch $PROJECT_DIR/$PROJECT_NAME/apps/users/api/serializers.py
    touch $PROJECT_DIR/$PROJECT_NAME/apps/users/api/views.py
    touch $PROJECT_DIR/$PROJECT_NAME/apps/users/api/parsers.py
    touch $PROJECT_DIR/$PROJECT_NAME/apps/users/api/permissions.py
    touch $PROJECT_DIR/$PROJECT_NAME/apps/users/api/renderers.py
    touch $PROJECT_DIR/$PROJECT_NAME/apps/users/api/validators.py
    touch $PROJECT_DIR/$PROJECT_NAME/apps/users/api/viewsets.py
    ```


### Notas:

Es posible comenzar a modularizar el proyecto, en especial cuando:

1. los modelos empiezan a crecer en atributos o métodos, y
2. cuando las views comienzar a tener mucha lógica. Esto incrementa el número de lineas en el archivo y lo hace complicado de leer.

- Ejemplo de app sin modularizar

  ```
  └── apps/
     └── users/
         ├── __init__.py
         ├── migrations/
         ├── admin.py
         ├── apps.py
         ├── models.py
         ├── tests.py
         └── views.py
  ```

- Ejemplo de app modularizada

  ```
  └── apps/
   └── sistema/
       ├── __init__.py
       ├── migrations/
       ├── admin.py
       ├── apps.py
       ├── tests.py
       ├── models.py
       ├── utils.py
       ├── templatetags/
       ├── templates/
       │   └── plan_internet/
       │      └── archivos.html
       ├── cache/
       │	 ├── __init__.py
       │   └── plan_internet_cache.py
       ├── tasks/
       │	 ├── __init__.py
       │   └── plan_internet_tasks.py
       ├── forms/
       │	 ├── __init__.py
       │   └── plan_internet_forms.py
       └── views/
           ├── __init__.py
           ├── plan_internet_views.py
           ├── ...
           └── router_views.py
  ```

Antes de pensar en modularizar como el ejemplo anterior hay que tener encuenta que realizar el import cuesta espacio en memoria. Por lo que consume menos memoria tener todos los modelos en un archivo que tener modelos o vistas divididos por archivos.

El modularizar dependera si la aplicación es altamente consumida (por ejemplo facturas en WispHub). En ese escenario debemos darle prioridad al performance que en la legibilidad. Pero si es una app que no es muy consumida pero sus modelos o vistas son extensos podemos dar prioridad a la legibilidad y modularizar

Una alternativa intermedia es mantener la siguiente estructura. Donde se modulariza unicamente el modelo mas extenso **Facturas** situandolo en el archivo `models/facturas.py` y todos los demas modelos se encuentran en `models/commons.py`

```
└── apps/
   └── wisp_facturas/
       ├── __init__.py
       ├── migrations/
       ├── admin.py
       ├── apps.py
       ├── tests.py
       ├── models/
       │   ├── __init__.py
       │   ├── commons.py
       │   └── facturas.py
       └── views.py
```


