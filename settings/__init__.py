from __future__ import absolute_import, unicode_literals
import os

os.environ.setdefault("DJANGO_LOG_LEVEL", "ERROR")

import pymysql

pymysql.install_as_MySQLdb()

# from ..server.celery import app

# __all__ = ("app",)
