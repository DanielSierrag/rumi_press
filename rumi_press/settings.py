"""
Django settings for rumi_press project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
from configurations import Configuration, values
from dj_database_url import parse as dburl
import os


class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-_zrc+qnt113@ii4=)t8ipm*+hd-s*-dsyhc-=9o%hfa6+t@r-1'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '172.21.0.1']

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.humanize',
        'rest_framework',
        'django_registration',
        'django.contrib.staticfiles',
        'debug_toolbar',
        'books.apps.BooksConfig',
        'books_auth.apps.BooksAuthConfig',
        'rest_framework.authtoken',
        'crispy_forms',
        'crispy_bootstrap5',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    ROOT_URLCONF = 'rumi_press.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    # Cookie configuration
    SESSION_COOKIE_AGE = 60 * 30  # 30 minutes
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    SESSION_SAVE_EVERY_REQUEST = True

    WSGI_APPLICATION = 'rumi_press.wsgi.application'

    # Logging congif
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
        },
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
                "filters": ["require_debug_false"],
            },
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }

    # Database
    # https://docs.djangoproject.com/en/5.2/ref/settings/#databases
    DATABASES = {}

    DB_USER = os.getenv('DATABASE_USER', 'root')
    DB_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', 'mypassword')
    DB_HOST = os.getenv('DATABASE_HOST', 'db')
    DB_PORT = os.getenv('DATABASE_PORT', 3306)
    DB_NAME = os.getenv('DATABASE_NAME', 'mydb')

    DATABASES['default'] = dburl(
        f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )

    # Email settings
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Password validation
    # https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

    AUTH_USER_MODEL = 'books_auth.User'

    LOGIN_REDIRECT_URL = '/accounts/profile/'
    LOGOUT_REDIRECT_URL = '/accounts/login/'

    # Cache config
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": "redis://redis:6379",
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/5.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value('America/Bogota')

    USE_I18N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.2/howto/static-files/

    STATIC_URL = 'static/'

    # Media
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # Default primary key field type
    # https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # Third-party apps settings

    # Crispy Forms Settings
    CRISPY_ALLOWED_TEMPLATE_PACKS = ['bootstrap5']
    CRISPY_TEMPLATE_PACK = 'bootstrap5'

    # Django registration
    ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window
    REGISTRATION_OPEN = False  # Disables registration until the site is ready for it

    # Django rest framework settings
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ],
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
    }

    # Django debug toolbar
    INTERNAL_IPS = ['localhost', '127.0.0.1', '172.21.0.1']


class Prod(Dev):
    DEBUG = False
