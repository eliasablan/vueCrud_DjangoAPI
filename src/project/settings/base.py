import os
from decouple import config as dc_config

BASE_DIR = os.path.dirname(
            os.path.dirname(
            os.path.dirname(
            os.path.abspath(__file__)
            )))

SECRET_KEY = dc_config('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'imagekit',
    'corsheaders',

    'blog_api',
    'core'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'project.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

VENV_PATH = os.path.dirname(BASE_DIR)

STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(VENV_PATH, 'media')

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
)
