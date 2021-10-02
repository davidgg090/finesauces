SECRET_KEY = '%fqh_p=v71rlnv0f^urdjffx#aq7n+_gzeznh)i28azuoycq*k'
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finesauces',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost'
        }
}