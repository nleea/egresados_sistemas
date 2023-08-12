from __future__ import absolute_import, unicode_literals
import pymysql
from .celery import app
import os

os.environ.setdefault("DJANGO_LOG_LEVEL","ERROR")

pymysql.install_as_MySQLdb()

__all__ = ("app",)