from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TWITTER_APP_KEY = os.environ.get("TWITTER_APP_KEY")
TWITTER_APP_SECRET = os.environ.get("TWITTER_APP_SECRET")
TWITTER_OAUTH_TOKEN = os.environ.get("TWITTER_OAUTH_TOKEN")
TWITTER_OAUTH_TOKEN_SECRET = os.environ.get("TWITTER_OAUTH_TOKEN_SECRET")
FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")
FACEBOOK_ACCESS_TOKEN = os.environ.get("FACEBOOK_ACCESS_TOKEN")

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')