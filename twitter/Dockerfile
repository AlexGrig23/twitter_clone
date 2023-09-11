# Використовуємо офіційний образ Python 3.9 як базу
FROM python:3.11

# Встановлюємо змінні середовища для Django
ENV PYTHONUNBUFFERED=1

# Створюємо та встановлюємо робочу директорію
WORKDIR /code

# Копіюємо файл залежностей та встановлюємо їх
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt


# Копіюємо весь проект у контейнер
COPY . /code/

#Давайте додамо команду для запуску Django сервера:
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#Запустити цей контейнер можна за допомогою команд:
#
#docker build -t my-django-app .
#docker run -p 8000:8000 my-django-app