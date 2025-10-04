# 🤖 Telegram Bot + Django REST API

Проект представляет собой интеграцию **Telegram-бота на Aiogram** с **Django REST API**, через который бот получает и отправляет данные.  
API создан с помощью **Django REST Framework**, а база данных — стандартная **SQLite** (используется по умолчанию).

---

## 🧩 Архитектура

Telegram Bot (Aiogram)
↓ (HTTP запросы через aiohttp)
Django REST API (DRF)
↓
SQLite Database

yaml
Копировать код

---

## ⚙️ Технологии

- **Python 3.10+**
- **Django 5+**
- **Django REST Framework**
- **Aiogram 3**
- **Aiohttp**
- **SQLite (по умолчанию)**

---

## 🚀 Установка и запуск

### 1️⃣ Клонирование репозитория
- git clone https://github.com/<твой_профиль>/<название_репозитория>.git
- cd <название_репозитория>
  
### 2️⃣ Установка зависимостей
- pip install -r requirements.txt
- pip install django djangorestframework aiogram aiohttp
  
### 3️⃣ Настройка Django
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
  
API будет доступен по адресу:
- 👉 http://127.0.0.1:8000/api/courses/

### 4️⃣ Настройка Telegram-бота
- Создай бота через @BotFather
- Получи TOKEN
- Укажи его в файле bot_api.py:
  
python

- TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
- API_URL = "http://127.0.0.1:8000/api/users/"
  
### 5️⃣ Запуск бота
- python bot_api.py
- 💬 Команды бота
  
- /start	Регистрирует пользователя в базе (отправляет POST на Django API)
- патом в баре поавится кнопки

## 🗂 Структура проекта

- project/
- │
- ├── core/
- │   ├── models.py        # Модель BotUser
- │   ├── serializers.py   # Сериализация модели
- │   ├── views.py         # ViewSet для REST API
- │   ├── urls.py          # Маршруты API
- │
- ├── bot_api.py           # Код Telegram-бота (Aiogram + aiohttp)
- │
- ├── manage.py
- └── requirements.txt
- 🔗 Пример REST API
- GET /api/users/
- Возвращает всех зарегистрированных пользователей:

## 🧠 Принцип работы
Этап	Что делает
1	Пользователь пишет /start
2	Бот отправляет POST-запрос на Django API
3	Django сохраняет данные пользователя в SQLite
4	При /users бот делает GET-запрос и получает JSON-список пользователей

🛠 Пример запроса из бота
python
Копировать код
async with aiohttp.ClientSession() as session:
    async with session.get(API_URL) as response:
        users = await response.json()
📄 Лицензия
Свободное использование в учебных целях.
