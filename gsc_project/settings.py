import os
import environ
from django.contrib.messages import constants as messages

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")


ALLOWED_HOSTS = [
    "127.0.0.1",
    "bcpiskp.herokuapp.com",
    "bcpiskp.org",
    "www.bcpiskp.org",
    "http://www.bcpiskp.org",
    "http://bcpiskp.org/",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party
    "crispy_forms",
    "admin_honeypot",
    # local
    "src.apps.SrcConfig",
    "staff",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gsc_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "src.context_processors.get_notice",
            ],
        },
    },
]

WSGI_APPLICATION = "gsc_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": env("DB_ENGINE"),
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASS"),
            "HOST": env("DB_HOST"),  # Or an IP Address that your DB is hosted on
            "PORT": env("DB_PORT"),
            # "OPTIONS": {
            #     "sql_mode": "traditional",
            # },
        }
    }

    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.sqlite3",
    #         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    #     }
    # }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTH_USER_MODEL = 'accounts.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "static-root")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

# crispy forms
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_FAIL_SILENTLY = False

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


LOGIN_URL = "/login"

# # SMTP SETTINGS
# if DEBUG:
#     EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# else:
#     EMAIL_BACKEND = env("EMAIL_BACKEND")
#     EMAIL_HOST = env("EMAIL_HOST")
#     EMAIL_USE_TLS = env("EMAIL_USE_TLS")
#     EMAIL_PORT = env("EMAIL_PORT")
#     EMAIL_HOST_USER = env("EMAIL_HOST_USER")
#     EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
