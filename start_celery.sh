#!/bin/bash

source .venv/bin/activate

mkdir -p logs

trap 'kill 0' SIGINT SIGTERM EXIT

celery -A celery_app worker -l info > logs/celery_worker.log 2>&1 &
celery -A celery_app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler > logs/celery_beat.log 2>&1 &

wait