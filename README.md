# 📢 Доска объявлений (Bulletin Board)

**Платформа для публикации объявлений с отзывами, аутентификацией и REST API.**  
Создана с использованием современных технологий: Django, DRF, Docker, JWT, PostgreSQL.

> 💡 Полностью покрыта тестами, соответствует PEP8, задокументирована, готова к деплою и собеседованию.

---

## 🚀 Описание

Проект представляет собой **аналог Avito или OLX**, где пользователи могут:
- Публиковать объявления (название, цена, описание)
- Оставлять отзывы под объявлениями
- Регистрироваться и входить через JWT
- Сбрасывать пароль по email
- Управлять контентом через админ-панель

API доступно через Swagger, фронтенд может быть подключён отдельно.

---

## 🛠 Используемые технологии

| Категория       | Технологии |
|----------------|----------|
| **Backend**     | Python 3.13, Django 6.0, Django REST Framework |
| **База данных** | PostgreSQL |
| **Аутентификация** | JWT, `django-rest-passwordreset` |
| **API**         | DRF, CORS, Swagger (drf-yasg), ReDoc |
| **Тестирование** | `pytest`, `factory-boy`, `pytest-cov`, `ruff` |
| **Деплой**      | Docker, docker-compose, Nginx, Gunicorn |
| **CI/CD**       | Готово к настройке через GitHub Actions |
| **Статика**     | `collectstatic`, отдача через Nginx |
| **Линтеры**     | `ruff`, `isort`, `autoflake` — автоматическое форматирование |

---

## ✅ Особенности проекта

- ✅ Кастомная модель пользователя без `username` (логин по email)
- ✅ Права доступа: только автор может редактировать
- ✅ Полное покрытие тестами (`pytest`)
- ✅ Соответствие PEP8 (исправлены `W292`, `F401`, `E302`)
- ✅ Докстринги в моделях, вьюсетах, методах
- ✅ Автоматизированная сборка через Docker
- ✅ Поддержка HTTPS (готово к Let's Encrypt)

---

## 📦 Установка и запуск (локально)

### 1. Клонируйте репозиторий
bash git clone https://github.com/MariyaM1982/Bulletin_board.git cd Bulletin_board

---

### 2. Создайте `.env` файл

Создайте `.env` в корне проекта:
env EMAIL_HOST_USER=your_email@gmail.com EMAIL_HOST_PASSWORD=your_app_password

> 🔐 Для Gmail:
> - Включите двухфакторную аутентификацию
> - Создайте [App Password](https://myaccount.google.com/apppasswords)
> - Используйте его как пароль

> 📄 Совет: добавьте `.env.example` в репозиторий (без реальных данных)

---

### 3. Запустите через Docker
bash docker-compose up --build

> ⏱ Первый запуск займёт 2–5 минут (установка зависимостей)

---

### 4. Создайте суперпользователя

В новом терминале:
bash docker-compose exec web python manage.py createsuperuser

Если ошибка с `username` — используйте shell:
bash docker-compose exec web python manage.py shell
python from django.contrib.auth import get_user_model User = get_user_model() User.objects.create_superuser(email='admin@example.com', password='admin123')

---

## 🌐 Доступные эндпоинты

| Эндпоинт | Описание |
|--------|--------|
| [http://localhost:8000/admin](http://localhost:8000/admin) | Админ-панель Django |
| [http://localhost:8000/swagger](http://localhost:8000/swagger) | Документация API (Swagger) |
| [http://localhost:8000/redoc](http://localhost:8000/redoc) | Альтернативная документация (ReDoc) |
| [http://localhost:8000/api/ads/](http://localhost:8000/api/ads/) | Список объявлений |
| [http://localhost:8000/api/reviews/](http://localhost:8000/api/reviews/) | Список отзывов |

---

## 🧪 Примеры использования API

### 🔹 Регистрация пользователя
bash curl -X POST http://localhost:8000/api/auth/users/
-H "Content-Type: application/json"
-d '{"email": "user@example.com", "password": "password123"}'

### 🔹 Получение JWT токена
bash curl -X POST http://localhost:8000/api/auth/jwt/create/
-H "Content-Type: application/json"
-d '{"email": "user@example.com", "password": "password123"}'

### 🔹 Создание объявления (с токеном)
bash curl -X POST http://localhost:8000/api/ads/
-H "Authorization: Bearer <ваш_токен>"
-H "Content-Type: application/json"
-d '{"title": "Ноутбук", "price": 25000, "description": "Отличное состояние"}'

### 🔹 Оставить отзыв
bash curl -X POST http://localhost:8000/api/reviews/
-H "Authorization: Bearer <ваш_токен>"
-H "Content-Type: application/json"
-d '{"text": "Хороший товар!", "ad": 1}'

---

## 🧩 Структура API

### Объявления (`/api/ads/`)
- `GET /` — список (с пагинацией по 4)
- `POST /` — создать (авторизованный)
- `GET /{id}/` — детали
- `PATCH /{id}/` — редактировать (автор или админ)
- `DELETE /{id}/` — удалить (автор или админ)

### Отзывы (`/api/reviews/`)
- `GET /` — список
- `POST /` — создать
- `PATCH /{id}/` — редактировать (только автор)
- `DELETE /{id}/` — удалить (автор или админ)

### Аутентификация (`/api/auth/`)
- `POST /users/` — регистрация
- `POST /jwt/create/` — вход
- `POST /jwt/refresh/` — обновление токена
- `POST /password_reset/` — сброс пароля

---

## 🧪 Запуск тестов
bash
Запуск всех тестов
python -m pytest
С отчётом о покрытии
python -m pytest --cov=ads --cov=users --cov-report=term-missing
HTML-отчёт (откройте в браузере)
python -m pytest --cov=ads --cov-report=html open htmlcov/index.html

> ✅ Покрытие > 85%  
> ✅ Все тесты проходят

---

## 📁 Структура проекта

Bulletin_board/ 
├── board_project/ # Настройки Django 
│ ├── settings.py 
│ └── urls.py 
├── ads/ # Объявления и отзывы 
│ ├── models.py # Ad, Review 
│ ├── views.py # ViewSets 
│ ├── serializers.py # ModelSerializers 
│ ├── permissions.py # IsReviewAuthorOrReadOnly 
│ ├── urls.py # Роутинг через DefaultRouter 
│ └── tests/ # pytest + factories 
├── users/ # Пользователи 
│ ├── models.py # Кастомный User 
│ ├── views.py # UserViewSet 
│ └── urls.py 
├── nginx/ # Конфиг Nginx 
│ └── nginx.conf 
├── .dockerignore 
├── .gitignore 
├── .env.example # Шаблон переменных окружения 
├── docker-compose.yml 
├── Dockerfile 
├── requirements.txt 
├── pytest.ini 
├── conftest.py # Инициализация Django для pytest 
├── pyproject.toml # Настройки ruff, isort 
├── README.md 
└── manage.py

---


## 🤝 Автор

**@MariyaM1982** — 2025  
📧 masha.dev.email@gmail.com (пример)  
🔗 [GitHub](https://github.com/MariyaM1982)

---

> ✅ Проект полностью готов к собеседованию, деплою и CI/CD!