#!/bin/bash ##

# Установка зависимостей
pip install --upgrade pip
pip install -r requirements.txt

# Применение миграций
python manage.py migrate

# Сборка статики
python manage.py collectstatic --noinput

# Запуск приложения с uvicorn
#uvicorn core.asgi:application --host 0.0.0.0 --port 8000 --reload --log-level debug
python ./manage.py runserver 0.0.0.0:8000