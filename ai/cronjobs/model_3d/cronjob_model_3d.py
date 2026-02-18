import schedule
import time
import requests
import random
from datetime import datetime

from ai.cronjobs.model_3d.data.prompts import MODEL_PROMPTS


URL = "http://192.168.1.103:7861/generate"

def my_cron(title: str, prompt: str, duration: int):
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Request. Wait...")
    
    try:
        
        print(f"Prompt: {prompt}")
        
        payload = {
            "title": title,
            "prompt": prompt,
            "seed": 0
        }
        
        response = requests.post(URL, json=payload)
        response.raise_for_status()  # lanza error si no es 200

        data = response.json()

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Response: {data}")

    except Exception as e:
        print(f"Error llamando API: {e}")




def main():
    
    def job():
        asset = random.choice(MODEL_PROMPTS)

        my_cron(
            asset["title"],
            asset["prompt"],
            60
        )

    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()