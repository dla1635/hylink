""" Production Settings """

import os
import dj_database_url
from .dev import *

############
# DATABASE #
############
DATABASES = {
    # 'default': dj_database_url.config(
    #     default=os.getenv('DATABASE_URL')
    # )
    'default' : {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.path.join(BASE_DIR, 'hylink'),
        'USER' : 'root',
        'PASSWORD' : 'root',
        'HOST' : 'localhost',        
        'PORT' : '3306'
    }
}


############
# SECURITY #
############

DEBUG = False
# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']
