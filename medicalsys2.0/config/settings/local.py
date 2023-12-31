#Configuración Local
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'dbempleado',
#        'USER': 'mpomeranietz',
#        'PASSWORD': 'admin',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}

 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

#MEDIA FILES
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,"media")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

LANGUAGE_CODE = "es-ar"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field



