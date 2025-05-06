
FROM python:3.13

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

#В последующем для продакшн
#CMD ["gunicorn", "feedback.wsgi:application", "--bind", "0.0.0.0:8000"]
