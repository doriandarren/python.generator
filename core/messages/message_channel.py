import os
import requests
from django.conf import settings

class MessageChannel:
    
    @staticmethod
    def send(text: str, title: str = "Title", is_error: bool = False) -> None:

        url = settings.MESSAGE_CHANNEL_URL
        if not url:
            return

        title = f"{title} {settings.APP_NAME} {settings.APP_ENV}"

        text = text[:500]

        payload = {
            "embeds": [{
                "title": title,
                "description": text,
                "color": 0xFF0000 if is_error else 0x00FF00,
            }]
        }

        try:
            requests.post(url, json=payload, timeout=5)
        except requests.RequestException:
            pass
