import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------
# Security
# --------------------

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

if DEBUG:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "local-development-secret-key-only-do-not-use-in-production-2026",
    )
else:
    SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "yasminvashagh.com",
    "www.yasminvashagh.com",
    ".vercel.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://yasminvashagh.com",
    "https://www.yasminvashagh.com",
]


# --------------------
# Applications
# --------------------

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "portfolio",
]


# --------------------
# Middleware
# --------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------
# URLs and application
# --------------------

ROOT_URLCONF = "yasmin_portfolio.urls"

WSGI_APPLICATION = "yasmin_portfolio.wsgi.application"
ASGI_APPLICATION = "yasmin_portfolio.asgi.application"


# --------------------
# Templates
# --------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]


# --------------------
# Internationalization
# --------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tehran"

USE_I18N = True
USE_TZ = True


# --------------------
# Static files
# --------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# --------------------
# Production security
# --------------------

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
X_FRAME_OPTIONS = "DENY"

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False


# --------------------
# Default primary key
# --------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"