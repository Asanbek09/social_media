from pathlib import Path
from django.urls import reverse_lazy
import os

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

SECRET_KEY = '*'
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'easy_thumbnails',
    'images',
    'account',
    'actions',
    'debug_toolbar',
    'social_django',
    'django_extensions',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': '*',
        'NAME': BASE_DIR / '*',
    }
}

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

PASSWORD_HASHERS = [ 
    'django.contrib.auth.hashers.PBKDF2PasswordHasher', 
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher', 
    'django.contrib.auth.hashers.Argon2PasswordHasher', 
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher', 
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details', 
    'social_core.pipeline.social_auth.social_uid', 
    'social_core.pipeline.social_auth.auth_allowed', 
    'social_core.pipeline.social_auth.social_user', 
    'social_core.pipeline.user.get_username', 
    'social_core.pipeline.user.create_user',
    'account.authentication.create_profile',
    'social_core.pipeline.social_auth.associate_user', 
    'social_core.pipeline.social_auth.load_extra_data', 
    'social_core.pipeline.user.user_details',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

SOCIAL_AUTH_FACEBOOK_KEY = '*'
SOCIAL_AUTH_FACEBOOK_SECRET = '*'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = '*'
SOCIAL_AUTH_TWITTER_SECRET = '*'

SOCIAL_AUTH_GOOGLE_KEY = '*'
SOCIAL_AUTH_GOOGLE_SECRET = '*'

if DEBUG:
    import mimetypes
    mimetypes.add_type('application/javascript', '.js', True)
    mimetypes.add_type('text/css', '.css', True)

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u : reverse_lazy('user_detail', args=[u.username])
}

INTERNAL_IPS = [
    '127.0.0.1',
]

REDIS_HOST = '*'
REDIS_PORT = 6379
REDIS_DB = 0