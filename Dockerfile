# Используем минимальный Python-образ
FROM python:3.11-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей
COPY requirements.txt requirements.txt

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем рабочую директорию
WORKDIR /app

# Копируем Python-скрипт
COPY ingest_data.py ingest_data.py

# Указываем команду по умолчанию
ENTRYPOINT ["python", "ingest_data.py"]
