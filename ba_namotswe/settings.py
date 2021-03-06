"""
Django settings for x project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n7@bmf88asdjo$=f#4---8gqchixi38r02@o^tlgyonm_##+2c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', ]

PROJECT_TITLE = 'Ba Namotswe'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'simple_history',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_rule_groups.apps.AppConfig',
    'ba_namotswe.apps.AppConfig',
    'ba_namotswe.apps.EdcAppointmentAppConfig',
    'ba_namotswe.apps.EdcBaseAppConfig',
    'ba_namotswe.apps.EdcConsentAppConfig',
    'ba_namotswe.apps.EdcIdentifierAppConfig',
    'ba_namotswe.apps.EdcRegistrationAppConfig',
    'ba_namotswe.apps.EdcLabAppConfig',
    'ba_namotswe.apps.EdcMetaDataAppConfig',
    'ba_namotswe.apps.EdcProtocolAppConfig',
    'ba_namotswe.apps.EdcTimepointAppConfig',
    'ba_namotswe.apps.EdcVisitTrackingAppConfig',
    'ba_namotswe_dashboard.apps.AppConfig',
]


if 'test' in sys.argv:
    # Ignore running migrations on unit tests -- speeds up tests.
    MIGRATION_MODULES = {
        "call_manager": None,
        "edc_appointment": None,
        "edc_code_lists": None,
        "edc_configuration": None,
        "edc_consent": None,
        "edc_content_type_map": None,
        "edc_data_manager": None,
        "edc_death_report": None,
        "edc_death_report": None,
        "edc_identifier": None,
        "edc_metadata": None,
        "edc_registration": None,
        "edc_rule_groups": None,
        "edc_sync": None,
        "edc_visit_schedule": None,
        "edc_visit_tracking": None,
        "lab_clinic_api": None,
        "lab_clinic_reference": None,
        "lab_packing": None,
        "ba_namotswe": None,
        'django_crypto_fields': None,
    }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ba_namotswe.urls'

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

WSGI_APPLICATION = 'ba_namotswe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'ba_namotswe', 'static')
GIT_DIR = BASE_DIR
CRISPY_TEMPLATE_PACK = 'bootstrap3'
KEY_PATH = os.path.join(BASE_DIR, 'crypto_fields')
ETC_DIR = os.path.join(BASE_DIR, 'etc')

STUDY_SITE = '10'
