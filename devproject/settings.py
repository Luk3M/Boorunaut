"""
Django settings for devproject project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@jh*9d-=6w3b7g6c!cxy(mjfpt+=$gj@4*tualb03$+dwset#z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'account.Account'

LOGIN_URL = 'account:login'

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'booru.account', # Needs to be migrated first
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    # Site apps
    'booru',
    'booru.core',
    # Dependency apps
    'taggit',
    'markdown_deux',
    'simple_history',
    'rolepermissions',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'devproject.urls'

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

                # Project processors
                'booru.context_processors.site_title',
                'booru.context_processors.site_description',
                'booru.context_processors.announcement',
                'booru.context_processors.custom_code',
            ],
        },
    },
]

WSGI_APPLICATION = 'devproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TAGGIT_CASE_INSENSITIVE = True
TAGGIT_TAGS_FROM_STRING = 'booru.utils.space_splitter'
TAGGIT_STRING_FROM_TAGS = 'booru.utils.space_joiner'

ROLEPERMISSIONS_MODULE = 'devproject.roles'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Boorunaut variables
BOORUNAUT_MAX_SIZE_FILE = 10 * 1024 * 1024
BOORUNAUT_INITIAL_UPLOAD_TIMEOUT = 2000
BOORUNAUT_MAXIMUM_UPLOAD_TIMEOUT = 2000

BOORUNAUT_INCLUDE_HEADER_CODE = '''
'''

BOORUNAUT_ADS_CODE = '''
'''
BOORUNAUT_ADS_ON_QUESTIONABLE = False
BOORUNAUT_ADS_ON_EXPLICIT = False

BOORUNAUT_EMBED_MODE = False
