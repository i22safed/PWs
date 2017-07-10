## Tutorial Django PW - Django 1.10.5 y Python 2.7

### 1. Primeros pasos  
#### 1.1. Creación del proyecto

Vamos al directorio en el cual queramos crear el proyecto y ejecutamos el comando

``` Django

     django-admin.py startproject "nombreproyecto"

```
Esto tendrá como resultado una sere de directorios.

#### 1.2. Creación de la aplicación

El próximo paso será crear la aplicación en cuestion, para ello nos vamos a donde
está el ```manage.py``` para ejecutar el siguiente comando.

``` Python

     python manage.py startapp "gestion"

```

El siguiente paso es declarar la aplicación en el fichero ```settings.py```, mas
concretamente en el apartado de ```INSTALLED_APPS``` quedando de la siguiente
manera:

``` Python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestión',
]

```

#### 1.3. Modelos

Ahora debemos irnos la fichero ```models.py```, y declarar los modelos con los
que trabajará la aplicación. A groso modo son clases las cuales están compuestas
por dos tipos de atributos, conjunto de variables (nombre, ciudad, entrenador) y  
métodos (guardar, valor de retorno)

Para la aplicación declararemos dos modelos

``` Python

     class Equipo(models.Model):
         name = models.CharField(primary_key=True, max_length=25)

               # Aqui debería de ir un tipo de campo models.Primary_key pero
               # daba errores

         foundation = models.IntegerField()
         city = models.CharField(max_length=25)
         stadium = models.CharField(max_length=25)
         coach = models.CharField(max_length=25)
         capacity = models.IntegerField()

         def storage(self):
             self.save()

         def __unicode__(self):
             return self.name

     class Jugador(models.Model):
         team = models.ForeignKey('Equipo')  # Indicamos que es clave foránea,
                                             # es decir que el ID es la primaria
                                             # de otra tabla

         playerName = models.CharField(max_length=25)
         nacionality = models.CharField(max_length=3)
         age = models.IntegerField()
         heigh = models.IntegerField()
         position = models.CharField(max_length=3)

         def storage():
             self.save()

         def __unicode__(self):
             return self.playerName


```

Una vez declarados los modelos debemos hacer la migración e introducirlos en el
admin.py para poder gestionarlos desde ahí tambien, para ello:

``` Python  
python manage.py migrate
python manage.py makemigration gestion

```

Una vez realizado este paso, el siguiente es ir al fichero admin.py e introducir
las siguientes lineas:

``` Python
     from django.contrib import admin
     from gestion.models import Equipo, Jugador   <-

     admin.site.register(Equipo)                  <-
     admin.site.register(Jugador)                 <-
```

Para poder acceder al admin de Django debemos introducir el comando ``` python
manage.py createsuperuser ``` introducimos los datos necesarios y aceptamos



#### 1.4. Urls

Necesitamos declarar las Urls en el fichero ```urls.py``` para despues poder
acceder a las vistas. [Continuar despues]

Primero indicamos en el fichero de URLs original ('practicas/urls.py') la
referencia a fichero de ('gestion/urls.py') ya que empezaremos son URLs especificas
de la aplicacion

``` Python
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('gestion.urls')),

]
```

Despues creamos el fichero de URLs de la aplicación, en el directorio gestion
(gestion/urls.py). Con el siguiente código:

``` Python

from django.conf.urls import include,url
from . import views
urlpatterns = [
        url(r'^$', views.team_list),
    ]

```

#### 1.5. Vistas

Una vez especificadas las URLs, es hora de crear el directorio de las vistas
dentro de la carpeta de la aplicación (gestion) un ejemplo de directorio es ``` gestion/templates/gestion/team_list.html ```. Dentro de este directorio creamos
la vista (.html).

Para poder ver la vista (.html) definimos en el fichero ``` views.py ``` el
siguiente método (tambien es necesario importar los modelos que hayamos creado),
un ejemplo de ```views.py``` sería el siguiente:

``` Python

from django.shortcuts import render
from .models import Equipo,Jugador

# Create your views here.

def team_list(request):
    return render(request, 'gestion/team_list.html',{})

```
