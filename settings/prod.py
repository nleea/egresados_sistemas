from settings.base import *

import os

DEBUG = False

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
