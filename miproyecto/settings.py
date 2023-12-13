"""
Django settings for miproyecto project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3imdsu$q2nou#wc7&ip1bp888)w*_61&wbtmfi6qnix&#m$j#z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    
    # ================================   Login
    'django.contrib.auth',
    # ================================   Permisos
    'django.contrib.contenttypes',
    # ================================
    
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Aplicaciones del proyecto
    'catalogos',
    'generales',
    'usuarios',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miproyecto.urls'
import os 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'miproyecto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'control.sqlite3',
    }
}


# Cliente de Base de Datos para PostgreSQL

# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'NAME': 'mibase',
#         'USER': 'usuario1',
#         'PASSWORD': 'abc123',
#     }
# }

# pip install psycopg2
# CREATE USER usuario1 WITH PASSWORD 'abc123';
# CREATE DATABASE mibase WITH OWNER usuario1;
# Python manage.py makemigrations
# Python manage.py migrate
# Python manage.py createsuperuser
# Python manage.py runserver

# Django 4.2 no es compatible con versiones anteriores a PostgreSQL 12 o posteriores
# Acciones
#
# pip uninstall django
# pip install django==4.1
# Listo !!!

'''
Necesita degradar su Django o actualizar su versión de PostgreSQL. Creo que degradar Django será más fácil. Para eso puedes hacer lo siguiente:
pip uninstall django
Después de la desinstalación, necesitas reinstalar django pero con una versión inferior, para eso puedes usar el siguiente comando:
pip install django==4.1
Django 4.2 no admite PostgreSQL inferior a 12 (como dijiste que tienes Django 4.2), pero Django 4.1 puede usar PostgreSQL 11.xx. Aquí está la documentación:

para Django 4.2: https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes
para Django 4.1: https://docs.djangoproject.com/en/4.1/ref/databases/#postgresql-notes
'''

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ===============================================
# REDIRECCIONAMIENTO PARA HACER Login Y Logout

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = 'login'
# ===============================================