"""
WSGI config for centro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from django.conf import settings
import environ

env = environ.Env()

ENV = env("ENV")
APPS = f"settings.{ENV}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", APPS)

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.MEDIA_ROOT)
# application.add_files("/path/to/more/static/files", prefix="more-files/")
