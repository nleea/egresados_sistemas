from __future__ import absolute_import, unicode_literals
import os
from configuration.settings.base import *

os.environ.setdefault("DJANGO_LOG_LEVEL", "ERROR")

import pymysql

pymysql.install_as_MySQLdb()

from .celery import app

__all__ = ("app",)
