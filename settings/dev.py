from settings.base import *

import os

DEBUG = True


DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

RENDER_PANELS = True

INTERNAL_IPS = ["127.0.0.1"]


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
