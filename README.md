# Django Calculator API (Homework)

Це навчальний проєкт на Django, створений для відпрацювання навичок роботи з API. Проєкт дозволяє виконувати розрахунки через POST-запити та зберігати дані в базі.

## 🛠 Технології
- Python 3.x
- Django 6.0.x
- Django REST (або базові JsonResponse)
- python-dotenv (для безпечного зберігання секретів)

## 🚀 Як запустити проєкт локально

### 1. Клонування репозиторію
```bash
git clone <url_вашого_репозиторію>
cd Django-Homework
```

### 2. Налаштування віртуального середовища
```Bash
python -m venv .venv
source .venv/bin/activate  # Для macOS/Linux
# або
.venv\Scripts\activate     # Для Windows
```

### 3. Встановлення залежностей
```Bash
pip install django python-dotenv
```

### 4. Налаштування змінних оточення
Створіть файл .env у кореневій папці на основі шаблону:

```Bash
cp .env.example .env
```
Відкрийте файл .env та додайте свій SECRET_KEY.


### 5. Запуск міграцій та сервера
```Bash
python manage.py migrate
python manage.py runserver
```


