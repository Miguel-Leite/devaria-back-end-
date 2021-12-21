import environ

from Core.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env.get('SECRET_KEY')

ALLOWED_HOSTS = env.get('ALLOWED_HOSTS')

DATABASES = {
    "default": env.db(),
}