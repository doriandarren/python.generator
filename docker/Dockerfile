FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    iputils-ping \
    cron \
    nano \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY docker/cron/generator-cron /etc/cron.d/generator-cron

RUN chmod 0644 /etc/cron.d/generator-cron && crontab /etc/cron.d/generator-cron