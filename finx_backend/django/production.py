from .base import *
from finx_backend.env import env

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

CORS_ALLOW_ALL_ORIGINS = False

CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST", default=[])
