"""
Django settings for AXF project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
'''
全局设置
'''

import os

# django默认的工程绝对路径
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# django默认的生成的全局秘钥
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^^!^gqh+ol=d1n8p976ll+(@+g04&_4*0=(0%@!-ul%2=9ge_c'

# DEBUG模式，默认True，部署生产环境时置为False
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 允许所有IP访问
ALLOWED_HOSTS = ["*"]

# Application definition

# 配置应用
INSTALLED_APPS = [

    # 默认的django应用

    # 站点管理
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 自定义的应用
    'App',
]

# django默认的中间件
MIDDLEWARE = [

    # django默认的中间件
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# django默认的路由文件
ROOT_URLCONF = 'AXF.urls'

# django默认的模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 模板路径
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

# django默认的WSGI配置
WSGI_APPLICATION = 'AXF.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# django默认的数据库配置
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# 配置数据库
DATABASES = {
    'default': {
        # 数据库引擎
        'ENGINE': 'django.db.backends.mysql',

        # 数据库名称
        'NAME': 'aixianfeng',

        # 账号和密码
        'USER': 'root',
        'PASSWORD': '123456',

        # IP和端口
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# django默认的密码校验器
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# django默认的国际化配置
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# django默认的静态文件访问路由
STATIC_URL = '/static/'

# 定义上传文件的路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads')

# 自定义静态文件的位置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 回归测试
if __name__ == '__main__':
    print(STATICFILES_DIRS)
    pass
