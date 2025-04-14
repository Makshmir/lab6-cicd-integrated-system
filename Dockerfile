# Використовуємо офіційний образ Python
FROM python:3.9-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл залежностей та встановлюємо їх
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту коду програми
COPY . .

# Відкриваємо порт, на якому працює додаток
EXPOSE 5000

# Команда для запуску додатку
CMD ["python", "app.py"]