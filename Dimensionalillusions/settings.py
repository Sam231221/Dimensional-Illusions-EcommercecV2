"""
Django settings for Dimensionalillusions project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=')osa2y(^uk4sdghs+#(14if-)b1&6_uo@(h#0c%sci^a#!(k@z'
#SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dimensionalilliusionversion1.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #CUSTOM  APPS
     'EHub.apps.EhubConfig',
     'EBlog.apps.EblogConfig',
     'VFX.apps.VfxConfig',     
     'SFX.apps.SfxConfig',   
     'GraphicsElements.apps.GraphicselementsConfig',
     'OTHERS.apps.OthersConfig',
     'SpecialPacks.apps.SpecialpacksConfig',
     'EDashboard.apps.EdashboardConfig',
     
     'mptt',
     'ckeditor',
     'taggit'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    

    'whitenoise.middleware.WhiteNoiseMiddleware', 
        
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Dimensionalillusions.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        'DIRS': [os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'Dimensionalillusions.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/staticfiles/'  #meaning- static url is /static/ which is a relative path and appears in url section .we dont need to mention statiic path in codes(links)

#MUST FOR LOADIN STATIC FILES
STATICFILES_DIRS=[         
    os.path.join(BASE_DIR, 'staticfiles')  
    ]
#This code implies that there is folder name staicfiles from which images, js ,cs are to be fetched.
#STATICFILES_DIRS is necesary for displaying images, css js from a folder(in this project 'staticfiles') that we define    

STATIC_ROOT=os.path.join(BASE_DIR, 'static')#This is a setup(an absolute path) for css,js files used when you deploy your web app.

#WHITENOISE CONFIGURATION
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#FOR SAVING IMAGES INTO THE 'static/images'
MEDIA_ROOT =os.path.join(BASE_DIR, 'staticfiles/mediafiles')  ## Path where media is stored
MEDIA_URL ='/mediafiles/'  #your relative url browser path for medias resdients.# Base url to serve media files

#meaning- Suppose you define a imagefield in customer model in models.py.So, for the image to be upload and save on the datatbase
# we need to specify a path where the images are gonna be layed down. 

#SMTP CONFIGURATION

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#THIS IS YOUR LOGIN INFO FOR GMAIL ADDRESS
EMAIL_HOST_USER = 'dimensionalassistanceteam37@gmail.com'
EMAIL_HOST_PASSWORD = '123@gmailcom'

#Your gmail is gonna send pw reset message to the client via gmail that they specify in password_reset_sent.html for password reset.
#The email that they provide is only gonna be effective and sent if the email exists in django database
