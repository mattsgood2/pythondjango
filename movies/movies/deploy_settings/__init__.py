from dj_database_url

from movies.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")

db_from-env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
