"""
Django settings for protected_static_site project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import copy
from pathlib import Path

import environ
from django.utils import log

# Don't generate translations for this file, import as _gettext_lazy
from django.utils.translation import gettext_lazy as _gettext_lazy

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(env.str("PROJECT_BASE_DIR", "")).resolve()

if env.bool("LOAD_DOTENV", True):
    environ.Env.read_env(BASE_DIR / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

INTERNAL_IPS = env.list("INTERNAL_IPS", default=[])

# Application definition

INSTALLED_APPS = [
    "domingues.protected_static_site.core",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "domingues.protected_static_site.urls"


# Raise an exception when accessing an undefined variable in templates
class InvalidString(str):
    def __mod__(self, other):
        from django.template.base import TemplateSyntaxError

        raise TemplateSyntaxError(f"Undefined variable or unknown value for: {other}")


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "string_if_invalid": InvalidString("%s"),
        },
    },
]

FORM_RENDERER = "django.forms.renderers.DjangoDivFormRenderer"

WSGI_APPLICATION = "domingues.protected_static_site.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

LOGIN_REDIRECT_URL = "profile"

LOGIN_URL = "login"

LOGOUT_REDIRECT_URL = "login"

# Force Django to log to terminal when DEBUG is false
# https://docs.djangoproject.com/en/4.2/topics/logging/
LOGGING = copy.deepcopy(log.DEFAULT_LOGGING)
LOGGING["handlers"]["console"]["filters"] = []

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

LANGUAGES = [
    ("en", _gettext_lazy("English")),
]

TIME_ZONE = "Europe/Lisbon"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"

SITE_DIR = BASE_DIR / env.str("SITE_DIR", "site_files")

SHOW_INDEXES = env.bool("SHOW_INDEXES", False)
