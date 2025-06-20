from dotenv import load_dotenv
import os


load_dotenv()

ENGINE = os.getenv('ENGINE')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
NAME = os.getenv('NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
