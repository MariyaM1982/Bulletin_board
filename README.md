# 📢 Доска объявлений (Bulletin Board)

Платформа для публикации объявлений с отзывами, аутентификацией и REST API.  
Создана на Django + Django REST Framework, упакована в Docker.

---

## 🚀 Функционал

- Публикация объявлений (название, цена, описание)
- Оставление отзывов к объявлениям
- Админ-панель для управления контентом
- Регистрация и аутентификация через JWT
- Сброс пароля по email
- Swagger UI для документации API
- Полностью покрыта тестами (`pytest`)
- Запуск в Docker (PostgreSQL, Gunicorn, Nginx)

---

## 🛠 Технологии

- **Backend**: Python 3.13, Django 6.0, DRF
- **База данных**: PostgreSQL
- **API**: JWT, CORS, Swagger (drf-yasg)
- **Тесты**: pytest, factory-boy
- **Деплой**: Docker, docker-compose
- **Статика**: collectstatic + Nginx

---

## 📦 Установка и запуск (локально)

### 1. Клонируйте репозиторий
bash git clone https://github.com/ваш-ник/Bulletin_board.git cd Bulletin_board

### 2. Создайте `.env` (не коммитится!)
env EMAIL_HOST_USER=ваш@gmail.com EMAIL_HOST_PASSWORD=ваш_токен
> Для Gmail: используйте "App Password"

---

### 3. Запустите через Docker
bash docker-compose up --build

После запуска:

- **API**: [http://localhost:8000/api/ads/](http://localhost:8000/api/ads/)
- **Swagger**: [http://localhost:8000/swagger](http://localhost:8000/swagger)
- **Админка**: [http://localhost:8000/admin](http://localhost:8000/admin)

> 🔐 Логин/пароль создаются через `createsuperuser` (см. ниже)

---

### 4. Создайте суперпользователя
bash docker-compose exec web python manage.py createsuperuser
Или через shell (если нет `username`):
bash docker-compose exec web python manage.py shell
python from django.contrib.auth import get_user_model User = get_user_model() User.objects.create_superuser(email='admin@example.com', password='admin123')

---

## 🧪 Запуск тестов
bash
Убедитесь, что вы в корне проекта
python -m pytest
С отчётом о покрытии
python -m pytest --cov=ads --cov=users --cov-report=term-missing
HTML-отчёт (откройте htmlcov/index.html)
python -m pytest --cov=ads --cov-report=html
---

## 🌐 Структура API

### Объявления
- `GET /api/ads/` — список
- `POST /api/ads/` — создать (авторизованный)
- `PATCH /api/ads/{id}/` — редактировать (только автор или админ)

### Отзывы
- `GET /api/reviews/` — список
- `POST /api/reviews/` — создать
- `PATCH /api/reviews/{id}/` — редактировать (только автор)

### Аутентификация
- `POST /api/auth/users/` — регистрация
- `POST /api/password_reset/` — сброс пароля

---

## 📁 Структура проекта
Bulletin_board/ 
├── board_project/ # Настройки Django 
├── ads/ # Объявления и отзывы 
├── users/ # Пользователи и аутентификация 
├── nginx/ # Конфиг Nginx 
├── docker-compose.yml 
├── Dockerfile 
├── requirements.txt 
├── pytest.ini 
└── README.md
---

## 🤝 Автор

@MariyaM1982 — 2025

---

> ✅ Проект полностью готов к деплою!

✅ Как использовать

Сохраните как README.md в корне проекта
Добавьте в Git:
git add README.md
git commit -m "docs: add README"
git push origin develop
