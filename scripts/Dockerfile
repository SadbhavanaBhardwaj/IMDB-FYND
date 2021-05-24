FROM python:3.8.3-alpine

WORKDIR /imdb-service/imdb

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .


RUN python3 manage.py migrate

RUN python3 manage.py loaddata scripts/groups.json

RUN python3 manage.py loaddata scripts/genre.json

