import dj_database_url
from movies.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")

db_from_env = dj_database_url.config('postgres://vygqqqdzifusjk:6f9e92348c2319fa66a17fa91df3fce43fc1ffd986b2c71aa372cd267b8ab92f@ec2-54-247-124-9.eu-west-1.compute.amazonaws.com:5432/ddf4m0tasds1qf')
DATABASES['default'].update(db_from_env)
