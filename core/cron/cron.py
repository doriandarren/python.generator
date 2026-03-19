from pathlib import Path

from django.utils import timezone

from core.messages.message_channel import MessageChannel

def hello_cron():
    
    now = timezone.now()
    
    MessageChannel.send(
        text=f"hello_cron ejecutado: {timezone.now()}",
        title="CRON",
    )
    
    log_path = Path("/Users/dorian/PythonProjects/python.generator/cron_test.log")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"[CRON] hello_cron ejecutado: {now}\n")
    
    print(f"[CRON] hello_cron ejecutado: {now}")
