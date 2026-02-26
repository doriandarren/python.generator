from django.utils import timezone

def hello_cron():
    print(f"[CRON] hello_cron ejecutado: {timezone.now()}")
