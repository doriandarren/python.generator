import schedule
import time
import requests
import random
from datetime import datetime

from ai.cronjobs.music.data.music_prompts import MUSIC_PROMPTS


## Music Long
URL_MUSIC = "http://192.168.1.103:7890/music"
URL_CONTINUE = "http://192.168.1.103:7890/music-loop-from-wav"


def my_cron(prompt: str, duration: int):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Request. Wait...")

    audio_music_path = ''

    try:

        payload = {
            "prompt": prompt,
            "duration": duration
        }

        response = requests.post(URL_MUSIC, json=payload)
        response.raise_for_status()  # lanza error si no es 200

        data = response.json()

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Response: {data}")

        full_music_path = data["audio_path"]
        audio_music_path = full_music_path.split("/")[-1]

    except Exception as e:
        print(f"Error llamando API: {e}")

    try:

        payload = {
            "filename": audio_music_path,
            "target_seconds": 600,
            "fade_ms": 3000,
            "circular": True
        }

        response = requests.post(URL_CONTINUE, json=payload)

    except Exception as e:
        print(f"Error: ")



def main():
    
    schedule.every(15).minutes.do(
        lambda: my_cron(
            random.choice(MUSIC_PROMPTS),
            60
        )
    )

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()
