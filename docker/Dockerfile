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

COPY docker/cron/root-crontab /etc/cron.d/root-crontab

RUN sed -i 's/\r$//' /etc/cron.d/root-crontab && \
    printf '\n' >> /etc/cron.d/root-crontab && \
    chmod 0644 /etc/cron.d/root-crontab && \
    crontab /etc/cron.d/root-crontab && \
    touch /var/log/app_scheduler.log

EXPOSE 8000