import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'JAFSD$%^&*YT^RASE%$T%ARSFDGYUASGDASUYUDasd123')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'debug_toolbar',
    'drf_yasg',
    'phonenumber_field',
    'rest_framework',

    'api.v1.general.apps.GeneralConfig',
    'api.v1.clients.apps.ClientsConfig',
    'api.v1.orders.apps.OrdersConfig',
    'api.v1.solarapiinfos.apps.SolarapiinfosConfig',
    'api.v1.services.apps.ServicesConfig',
    'api.v1.products.apps.ProductsConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (str(BASE_DIR) + '/static_files',)
STATIC_ROOT = str(BASE_DIR) + '/static'
MEDIA_URL = 'media/'
MEDIA_ROOT = str(BASE_DIR) + '/media'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SOLAR_API_KEY = os.environ.get("API_KEY")
SOLAR_API_REQUIRED_QUALITY = "MEDIUM"

BUILDING_INSIGHTS = "https://solar.googleapis.com/v1/buildingInsights:findClosest"

CLIENT_APPS = ['customers', 'services', 'solarapiinfos']
CLIENT_MAX_SERVICES = 10
ADMIN_SITE_HEADER = 'Suncount.io'

SERVICE_LIMIT = 20
PRODUCT_LIMIT = 5

LESS_LIMIT_REQUEST = 50

# smtp configs
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        }
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

if DEBUG:
    INTERNAL_IPS += [
        "admin.suncount.io"
    ]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "https://suncount.io",
]

MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_ORDER_TABLE = os.environ.get('MYSQL_ORDER_TABLE')
MYSQL_USER_TABLE = os.environ.get('MYSQL_USER_TABLE')
MYSQL_CUSTOMER_TABLE = os.environ.get('MYSQL_CUSTOMER_TABLE')
MYSQL_PRODUCT_TABLE = os.environ.get('MYSQL_PRODUCT_TABLE')
ORDER_EXPIRE_DAYS = int(os.environ.get('ORDER_EXPIRE_DAYS'))

CELERY_BROKER_URL = 'redis://localhost:6379/0'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'api.v1.clients.permissions.IsMYSQLClient',
    ),
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M',

}
