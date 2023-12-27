from settings.base import *

import os

DEBUG = False

MIDDLEWARE = [
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "configs.middlewares.auth.CustomMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "configs.middlewares.loggin_middleware.LoggingMiddleware",
    "configs.middlewares.view_responses.CustomResponseMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_DEVELOP_NAME"),
        "USER": os.environ.get("DB_DEVELOP_USER"),
        "PASSWORD": os.environ.get("DB_DEVELOP_PASSWORD"),
        "HOST": os.environ.get("DB_DEVELOP_HOST"),
        "PORT": os.environ.get("DB_DEVELOP_PORT"),
    },
}
