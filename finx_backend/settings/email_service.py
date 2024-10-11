from finx_backend.env import env

if env.bool('DJANGO_DEBUG', default=True) == True:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
