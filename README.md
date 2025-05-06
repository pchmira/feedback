
# Форма обратной связи

## Описание

Это проект на Django, который реализует форму обратной связи 
для сервисного портала с возможностью отправки различных типов обращений. 
В проекте используется 
Django REST Framework для работы с API и PostgreSQL как база данных.

## Функциональность

- Пользователь может выбрать тип обращения из выпадающего списка (пожелание, проблема, претензия, другое).
- Пользователь может описать суть обращения в текстовом поле.
- Пользователь может прикрепить файл (по желанию).
- Данные формы сохраняются в базе данных.
- Ответ от API подтверждает успешную отправку сообщения или выводит ошибки валидации.

## Требования
- Python 3.x
- PostgreSQL
- Docker (опционально)


## Установка локальная

1. Клонируйте репозиторий:
    ```bash
    git clone <URL_вашего_репозитория>
    cd feedback_form
    ```

2. Создайте виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scriptsctivate     # Для Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Настройте переменные окружения:
    - Создайте файл `.env` в корне проекта.
    - Пример содержимого лежит в .env.example

5. Выполните миграции: 
    ```bash
    python manage.py migrate
    ```
6. Запустите сервер разработки: 
    ```bash
    python manage.py runserver
    ```
   
## Запуск через Docker

1. Запустите контейнеры с помощью Docker Compose:
    ```bash
    docker-compose up --build
    ```

2. Примените миграции:
    ```bash
    docker-compose exec feedback-web python manage.py migrate
    ```

3. (Опционально) Создайте суперпользователя для доступа к Django Admin:
    ```bash
    docker-compose exec feedback-web python manage.py createsuperuser
    ```

## Разработка

- Для запуска проекта используйте:
    ```bash
    docker-compose up
    ```

- Для запуска тестов:
    ```bash
    docker-compose exec feedback-web python manage.py test
    ```

## Структура проекта

- `feedback/` - Приложение Django, реализующее форму обратной связи.
- `Dockerfile` - Docker конфигурация для запуска Django.
- `docker-compose.yml` - Составляющие Docker контейнеров (Django, PostgreSQL).
- `requirements.txt` - Список зависимостей для Python.

## Примечания

- Проект использует PostgreSQL в Docker контейнере.
- Файлы базы данных хранятся внутри контейнера `feedback-db`.
- Для доступа к API используйте URL: `http://localhost:8000/api/feedback/`.
- Для доступа к форме на фронте: `http://localhost:8000/feedback/`.

