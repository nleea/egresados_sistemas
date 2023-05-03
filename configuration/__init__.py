from __future__ import absolute_import, unicode_literals
import pymysql
from .celery import app

pymysql.install_as_MySQLdb()

__all__ = ("app",)