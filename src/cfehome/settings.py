
from pathlib import Path
import os
from decouple import Config
config = Config(search_path='C:\Users\LEGION\Desktop\SAAS\src\cfehome\.env')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# tried to use python decoupling but it is not working. 
DJANGO_SECRET_KEY = config("DJANGO_SECRET_KEY",default='django-insecure-ib38!1c9yfvddmkwmce*9j9l5lvgvl8xr)306629j@006#7&o0')
DJANGO_DEBUG = config("DJANGO_DEBUG",cast=bool,default=0)

from decouple import Config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
config = Config(BASE_DIR / '.env')
ALLOWED_HOSTS = [
    ".railway.app",
]
if DJANGO_DEBUG:
    ALLOWED_HOSTS +=[
        "127.0.0.1",
        "localhost"
    ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'commando',
    'visits',
    
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

ROOT_URLCONF = 'cfehome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'src', 'visits', 'templates')],
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

WSGI_APPLICATION = 'cfehome.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CONN_MAX_AGE = config("CONN_MAX_AGE",cast=int,default=30)
DATABASE_URL=config("DATABASE_URL",default=None)
#if the postgres sql is not available, the the database will use sqllite database. 

if DATABASE_URL is not None:
    import dj_database_url
    DATABASES={
        "default":dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=CONN_MAX_AGE,
            conn_health_checks=True,
        )
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_BASE_DIR = BASE_DIR/"staticfiles"
STATICFILES_BASE_DIR.mkdir(exist_ok=True,parents=True)
STATICFILES_VENDOR_DIR= STATICFILES_BASE_DIR/"vendors"

#sources for python manage.py collectstatic
STATICFILES_DIRS=[
    STATICFILES_BASE_DIR
]

#output for python manage.py collectstatic
STATIC_ROOT= BASE_DIR.parent/"local-cdn"
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
