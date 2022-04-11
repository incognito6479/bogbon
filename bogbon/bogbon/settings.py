# Django 3.1.4

# ExternalImports
from pathlib import Path
import os
# End ExternalImports


# BaseDir
BASE_DIR = Path(__file__).resolve().parent.parent
# End BaseDir

# SecurityKey
SECRET_KEY = 'q376@h@(+_wdrbbo9e3w9g*n*7j2=-mxp9k+2idl24nmc+5k4s'
# End SecurityKey

# DebugMode
DEBUG = True
# End DebugMode

# AllowedHosts
ALLOWED_HOSTS = ['*', ]
# End AllowedHosts

# ApplicationConfig
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp.apps.MainappConfig',
    'django_summernote',
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

ROOT_URLCONF = 'bogbon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bogbon.wsgi.application'
# End ApplicationConfig

# DatabaseConfig
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bogbon',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'OPTIONS': {
               'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
               'charset': 'utf8mb4',
        }
    }
}
# End DatabaseConfig

# PasswordValidation
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
# End PasswordValidation

# Internationalization
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Samarkand'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# End Internationalization

# StaticAndMedia
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mainapp/static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mainapp/media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

X_FRAME_OPTIONS = 'SAMEORIGIN'
# End StaticAndMedia
