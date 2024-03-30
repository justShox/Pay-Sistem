# Какой язык программирования и версия
FROM python:latest
# Устанавливаем все библиотеки
WORKDIR /PaySistem
# Копруем наш проект внутри папки(Docker)
COPY . /PaySistem

RUN pip install -r requirements.txt

# Команда для запуска
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=2524"]
