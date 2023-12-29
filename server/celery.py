from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import environ

env = environ.Env()
ENV = env("ENV")

APPS = f"settings.{ENV}"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", APPS)

app = Celery("sistema_egresados")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.enable_utc = False

app.conf.update(timezone="America/Bogota")

app.autodiscover_tasks()
