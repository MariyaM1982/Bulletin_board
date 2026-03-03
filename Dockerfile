# Используем официальный образ Python
FROM python:3.13-slim

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=board_project.settings

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Экспонируем порт (по умолчанию 8000)
EXPOSE 8000

# Команда запуска
CMD ["gunicorn", "board_project.wsgi:application", "--bind", "0.0.0.0:8000"]