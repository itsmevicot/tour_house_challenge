SECRET_KEY = 'django-insecure-l#)bn#ygmdg7!wcn0_7mir3s2ic1)$#!h5f(+lc%7c$3(rs(nj'

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tourhouse_challenge',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
