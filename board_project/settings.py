import os
from datetime import timedelta
from pathlib import Path

import dj_database_url
from decouple import config

# === Основные настройки ===
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-pd0rjx1&l0*u*fg^!@=phu&hcj()xk0nun9amk576e__^rce$y"

DEBUG = True

ALLOWED_HOSTS = ["*"]  # Только для разработки

# === CORS Настройки ===
CORS_URLS_REGEX = r"^/api/.*$"  # CORS только для /api/

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# 🔥 Обязательно для POST-запросов (включая админку при CORS)
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# === Приложения ===
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "drf_yasg",
    "users",
    "django_rest_passwordreset",
    "ads",
    "django_filters",
]

# === Middleware ===
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # ← Должен быть первым!
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "board_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "board_project.wsgi.application"

# База данных — всегда PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}

# === Валидация паролей ===
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# === Локализация ===
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# === Статика ===
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# === Пользовательская модель ===
AUTH_USER_MODEL = "users.User"

# === REST Framework ===
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "board_project.pagination.AdPagination",
    "PAGE_SIZE": 4,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# === JWT ===
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
}

# === Email ===
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')

# === Swagger ===
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Введите: Bearer <ваш_токен>\n\nПример: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx",
        }
    },
    "USE_SESSION_AUTH": False,
    "JSON_EDITOR": True,
    "SHOW_REQUEST_HEADERS": True,
}

SWAGGER_USE_COMPAT_RENDERERS = False

SECRET_KEY = config('SECRET_KEY')