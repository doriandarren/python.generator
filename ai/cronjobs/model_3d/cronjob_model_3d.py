import schedule
import time
import requests
import random
from datetime import datetime


def my_cron():
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Request. Wait...")
    






def main():
    
    ## First cron
    my_cron(random.choice([1, 2]), 60)
    
    schedule.every(15).minutes.do(
        lambda: my_cron(
            random.choice([1, 2]),
            60
        )
    )

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()