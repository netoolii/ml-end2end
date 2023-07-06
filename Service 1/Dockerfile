FROM python:3.9-slim

ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./app /app

WORKDIR /app

RUN pip install -U pip setuptools

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "gunicorn", "app:app", "--config=helpers/gunicorn/gunicorn.config.py"]