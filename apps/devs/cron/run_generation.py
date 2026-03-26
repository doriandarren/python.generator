from django.utils import timezone

from core.messages.message_channel import MessageChannel


def start():
    MessageChannel.send(
        text=f"hello_cron ejecutado: {timezone.now()}",
        title="CRON",
    )