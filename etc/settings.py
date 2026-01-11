import configparser

from common.constants import Constants

config = configparser.ConfigParser()
config.read([".env", ".secrets"])

Constants.readEnv(config)

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]
CORS_ALLOW_ALL_ORIGINS = True

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    "common",
]

ROOT_URLCONF = "urls"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": config["mysql"]["DB_DATABASE"],
#         "HOST": config["mysql"]["DB_HOST"],
#         "PORT": config["mysql"]["DB_PORT"],
#         "USER": config["mysql"]["DB_USERNAME"],
#         "PASSWORD": config["mysql"]["DB_PASSWORD"],
#
#     }
# }

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

USE_TZ = True
TIME_ZONE = "UTC"

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]