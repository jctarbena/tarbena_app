"""
Django settings for tarbena project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from django.core.signing import Signer
import os
import socket
HOSTNAME = socket.gethostname()
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/1.11/topics/signing/
if HOSTNAME == 'servidor':
    with open('/home/admin/files/django_secret_key.txt') as f:
        SECRET_KEY = f.read().strip()
else:
    from .django_secrets import SECRET_VALUE
    SECRET_KEY = SECRET_VALUE

# Ajax call to notify x update notifications every 5mins
NOTIFY_UPDATE_TIME_INTERVAL = 300000

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'flat_responsive',
    'colorfield',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'admin_honeypot',
    'subvenciones',
    'parcelas',
    'profiles',
    'martor',
    'smart_selects',
    'notify',
    'django_filters',
    'holidays',
    'rest_framework',
    'favourites',
    'gym',
    'contracts',
    'import_export',
    'museo',
    'terceros',
    'luz',
    'django_cleanup.apps.CleanupConfig',
    'UPR',
    #'pipeline',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
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

ROOT_URLCONF = 'config.urls'

LOGIN_REDIRECT_URL = reverse_lazy('index')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'subvenciones/templates'),
                 os.path.join(BASE_DIR, 'profiles/templates'),
                 os.path.join(BASE_DIR, 'parcelas/templates'),
                 os.path.join(BASE_DIR, 'contracts/templates'),
                 os.path.join(BASE_DIR, 'museo/templates'),
                 os.path.join(BASE_DIR, 'luz/templates'),
                 os.path.join(BASE_DIR, 'UPR/templates'),],
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
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "subvenciones/static"),
    os.path.join(BASE_DIR, "profiles/static"),
    os.path.join(BASE_DIR, "contracts/static"),
    os.path.join(BASE_DIR, "museo/static"),
    os.path.join(BASE_DIR, "luz/static"),
    os.path.join(BASE_DIR, "UPR/static"),
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Email server
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'agoraweb700@gmail.com'

if HOSTNAME == 'servidor':
    with open('/home/admin/files/django_secret_email.txt') as f:
        EMAIL_HOST_PASSWORD = f.read().strip()
else:
    from .django_secrets import SECRET_EMAIL_PASSWORD
    EMAIL_HOST_PASSWORD = SECRET_EMAIL_PASSWORD

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'agoraweb700@gmail.com'

# To receive server errors to my inbox
ADMINS = (
    ('Amos', 'agoraweb700@gmail.com'),
    ('Developer', 'amosisa700@gmail.com'),
)
MANAGERS = ADMINS


# Global martor settings
# Input: string boolean, `true/false`
MARTOR_ENABLE_CONFIGS = {
    'imgur': 'false',     # to enable/disable imgur/custom uploader.
    'mention': 'true',  # to enable/disable mention
    'jquery': 'true',    # to include/revoke jquery (require for admin default django)
}


# To setup the martor editor with label or not (default is False)
MARTOR_ENABLE_LABEL = True

# Imgur API Keys
# MARTOR_IMGUR_CLIENT_ID = 'your-client-id'
# MARTOR_IMGUR_API_KEY   = 'your-api-key'

# Safe Mode
MARTOR_MARKDOWN_SAFE_MODE = True # default

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default

# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins', # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention', # require for mention
    'martor.extensions.emoji',   # require for emoji
]

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
MARTOR_UPLOAD_URL = '/martor/uploader/' # default
MARTOR_SEARCH_USERS_URL = '/martor/search-user/' # default

# Markdown Extensions
MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://assets-cdn.github.com/images/icons/emoji/' # default
MARTOR_MARKDOWN_BASE_MENTION_URL = '#' # default (change this)

# Check this setting is not set else csrf will not be sent over ajax calls
CSRF_COOKIE_HTTPONLY = False


# Message tags
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# The max number of fields you can delete on admin site
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# Manage static files/assets with pipeline
#PIPELINE_YUGLIFY_BINARY = 'C:/Users/AMOS/AppData/Roaming/npm/node_modules/yuglify/bin/yuglify'
# COMPRESS_CSS_FILTERS = ["compressor.filters.yuglify.YUglifyCSSFilter"]
# COMPRESS_JS_FILTERS = ["compressor.filters.yuglify.YUglifyJSFilter"]
# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'pipeline.finders.PipelineFinder',
# )
#
# PIPELINE = {
#     'PIPELINE_ENABLED': True,
#     'STYLESHEETS': {
#         'museocss': {
#             'source_filenames': (
#               'museo/css/base.css',
#             ),
#             'output_filename': 'museo/css/base.min.css',
#         },
#     }
# }
#
# PIPELINE_COMPILERS = (
#     'pipeline.compilers.sass.SASSCompiler',
# )