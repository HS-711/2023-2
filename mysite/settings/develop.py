# SECURITY WARNING: keep the secret key used in production secret!
from .base import *

SECRET_KEY = "django-insecure-%vcbz#dku0t=y+igyp(q8ro8-&moh3&3ma^1%e9dl6u9p%fex("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
