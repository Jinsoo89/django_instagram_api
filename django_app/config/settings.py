"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import json
import os

DEBUG = os.environ.get('MODE') == 'DEBUG'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

# Template
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Config
CONF_DIR = os.path.join(ROOT_DIR, '.conf-secret')
CONFIG_FILE_COMMON = os.path.join(CONF_DIR, 'settings_common.json')

# Static
STATIC_DIR = os.path.join(BASE_DIR, 'static')
BOWER_DIR = os.path.join(ROOT_DIR, 'bower_components')
STATICFILES_DIRS = [
    STATIC_DIR,
    BOWER_DIR,
]
STATIC_URL = '/static/'

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Login redirect
LOGIN_URL = '/admin/'

if DEBUG:
    CONFIG_FILE = os.path.join(CONF_DIR, 'settings_local.json')
else:
    CONFIG_FILE = os.path.join(CONF_DIR, 'settings_deploy.json')

config_common = json.loads(open(CONFIG_FILE_COMMON).read())
config = json.loads(open(CONFIG_FILE).read())

for key, key_dict in config_common.items():
    if not config.get(key):
        config[key] = {}
    for inner_key, inner_key_dict in key_dict.items():
        config[key][inner_key] = inner_key_dict

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['django']['secret_key']
# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = config['django']['allowed_hosts']

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 2,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    )
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'member',
    'post',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
)
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config['db']['engine'],
        'NAME': config['db']['name'],
        'USER': config['db']['user'],
        'PASSWORD': config['db']['password'],
        'HOST': config['db']['host'],
        'PORT': config['db']['port'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'member.MyUser'
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True
