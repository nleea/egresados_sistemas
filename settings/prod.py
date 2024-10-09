from settings.base import *
import environ


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

env = environ.Env()
DB_DEVELOP_NAME = env("DB_DEVELOP_NAME")
DB_DEVELOP_USER = env("DB_DEVELOP_USER")
DB_DEVELOP_PASSWORD = env("DB_DEVELOP_PASSWORD")
DB_DEVELOP_HOST = env("DB_DEVELOP_HOST")
DB_DEVELOP_PORT = env("DB_DEVELOP_PORT")
REDIS = env("REDIS")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": DB_DEVELOP_NAME,
        "USER": DB_DEVELOP_USER,
        "PASSWORD": DB_DEVELOP_PASSWORD,
        "HOST": DB_DEVELOP_HOST,
        "PORT": DB_DEVELOP_PORT,
    },
}

# CACHE_TTL = 60 * 15

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": REDIS,
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         },
#         "KEY_PREFIX": "cache",
#     }
# }
