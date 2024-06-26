FROM python:3.9-slim


ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN pip install -U pip setuptools

COPY ./app/requirements.txt app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "gunicorn", "app:app", "--config=helpers/gunicorn.config.py", "--reload" ]