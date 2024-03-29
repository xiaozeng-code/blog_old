"""
Django settings for blogsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%6cx=nqha5ei3#n2d4gbgv_a2&=0l=)%k#^#&@vo2qnk1a8b_d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'taggit',
    'taggit_labels',
    'ckeditor',
    'blog',
    'photologue',
    'sortedm2m',
#    'grappelli',
#    'filebrowser',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blogsite.urls'

WSGI_APPLICATION = 'blogsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default':{
            'ENGINE':'django.db.backends.mysql',
            'NAME':'blog',
            'USER':'root',
            'PASSWORD':'aixocm',
            'HOST':'',
            'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

#USE_TZ = True
USE_TZ = False 

TIME_ZONE = 'Asia/Shanghai'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static/'),
    '/root/djaspace/blog/blog_static_dir',
)

STATIC_ROOT='/root/djaspace/blog/resources/static'


#Media files
MEDIA_URL='/media/'
MEDIA_ROOT="/tmp/media"

CKEDITOR_UPLOAD_PATH='uploads/'

CKEDITOR_RESTRICT_BY_USER=True

CKEDITOR_JQUERY_URL='/static/js/jquery.min.js'

CKEDITOR_IMAGE_BACKEND = 'pillow'


#CKEDITOR configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
            ['div','Source','-','Save','NewPage','Preview','-','Templates'], 
            ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'], 
            ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'], 
            ['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'], 
            ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'], 
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'], 
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'], 
            ['Link','Unlink','Anchor'], 
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'], 
            ['Styles','Format','Font','FontSize'], 
            ['TextColor','BGColor'], 
            ['Maximize','ShowBlocks','-','About', 'pbckcode'],
        ),
    }
}



SITE_ID=1
