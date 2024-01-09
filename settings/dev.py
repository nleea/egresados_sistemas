from settings.base import *
import environ

import os

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.gzip.GZipMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "configs.middlewares.view_responses.CustomResponseMiddleware",
]

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


env = environ.Env()
DB_DEVELOP_NAME = env("DB_DEVELOP_NAME")
DB_DEVELOP_USER = env("DB_DEVELOP_USER")
DB_DEVELOP_PASSWORD = env("DB_DEVELOP_PASSWORD")
DB_DEVELOP_HOST = env("DB_DEVELOP_HOST")
DB_DEVELOP_PORT = env("DB_DEVELOP_PORT")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_DEVELOP_NAME,
        "USER": DB_DEVELOP_USER,
        "PASSWORD": DB_DEVELOP_PASSWORD,
        "HOST": DB_DEVELOP_HOST,
        "PORT": DB_DEVELOP_PORT,
    },
}
