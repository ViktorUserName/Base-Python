``````oinkeeper_project/
├── coinkeeper_project/   # Настройки проекта
│   ├── __init__.py
│   ├── settings.py       # Настройки Django
│   ├── urls.py           # Главный роутинг
│   ├── asgi.py
│   └── wsgi.py
│
├── users/                # Приложение для пользователей
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Кастомная модель User (если нужно)
│   ├── urls.py           # Роуты для auth
│   ├── views.py          # Логика регистрации, логина и т.д.
│   ├── forms.py          # Форма для регистрации (если будет)
│   └── migrations/
│
├── wallet/               # Приложение для транзакций
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Category, Transaction
│   ├── urls.py           # Роуты для транзакций
│   ├── views.py
│   └── migrations/
│
├── manage.py
└── requirements.txt```