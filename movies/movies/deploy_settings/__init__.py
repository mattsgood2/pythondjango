import dj_database_url
from movies.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
