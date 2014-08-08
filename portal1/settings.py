"""
Django settings for nsa_collaboration project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# from  django.contrib.auth.models import User
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ey^!o9&^^2%aqzqspq7g$fn!fv#lxd_^pstq9w#rb-v_$w(e1x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'signup',
    'project',
    'address',
    'state',
    'company',
    'south',
    'rfc',
    'django_tables2',
    'rest_framework',
    'crispy_forms',
    'debug_toolbar'
)
CRISPY_TEMPLATE_PACK = 'bootstrap3'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'portal1.urls'

WSGI_APPLICATION = 'portal1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)
#STATIC_ROOT = (os.path.join(__file__, "static",)),

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#template Location
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "static", "templates")),

#"/Users/arashaga/Documents/Django_Projects/nsa/nsa_collaboration/static/"


MEDIA_URL = "/media/"
STATIC_ROOT = (os.path.join(BASE_DIR, 'static'))  # this is where Django finds all the collected files
MEDIA_ROOT = (os.path.join(BASE_DIR, "static", "media"))
STATICFILES_DIRS = (os.path.join(BASE_DIR,
                                 'static-only')),  #this is where you save all of your static and then collect them

AUTH_USER_MODEL = 'signup.SignUp'

ANONYMOUS_USER_ID = -1


# THIS IS IMPORTANT YOU NEED TO INCLUDE THIS TO GET YOUR TEST GOING
import sys

if 'test' in sys.argv:
    SOUTH_TESTS_MIGRATE = False
