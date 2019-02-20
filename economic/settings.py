"""
Django settings for economic project.

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

# Change to true before deploying into production
ENABLE_SSL = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x3pu8!zp7%ds4mlbgj+v@@!est3f1%j#c%p52(1#ns9%x-q1#2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Site id
SITE_ID = 1

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'preview.apps.PreviewConfig',
    'catalog.apps.CatalogConfig',
    'utils.apps.UtilsConfig',
    'cart.apps.CartConfig',
    'accounts.apps.AccountsConfig',
    'payment.apps.PaymentConfig',
    #'paypal.standard.ipn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'economic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'utils.context_processors.economic',
            ],
        },
    },
]

WSGI_APPLICATION = 'economic.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'economic',
        'USER': 'root',
        'PASSWORD': 'Immaculate0',
        'HOST': '127.0.0.1',
        'PORT': '3306',
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

# media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

SITE_NAME = 'Modern Laptop Solutions'
META_KEYWORDS = 'Computers, Laptops(Personal Computers), Computer accessories, Tech supplies'
META_DESCRIPTION = 'Modern Laptop Solutions is an online supplier of Laptops,Personal Computers, and computers related  accessories for ' \
                   'computer solutions '

# account for which users will be redirected to after they login
LOGIN_REDIRECT_URL = '/accounts/my_account/'


# django-paypal settings
PAYPAL_RECEIVER_EMAIL = "21325482f@gmail.com"
PAYPAL_TEST = True
#PAYPAL_URL = "https://api.sandbox.paypal.com/"+"access_token$sandbox$nxkqb2z5ztyvq6mp$e8f1491427d66d1a0200e0dd0ee45eca"
