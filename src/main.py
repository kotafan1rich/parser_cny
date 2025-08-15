from datetime import datetime
import time
import requests
from config import settings


BASE_URL = "https://iss.moex.com/iss/statistics/engines/futures/markets/indicativerates/securities/CNY/RUB.json"


def main():
    while True:
        date_now = datetime.now()
        year = date_now.year
        month = date_now.month
        day = date_now.day
        params = [
            ("lang", "ru"),
            ("from", f"{year}-{month}-{day}"),
            ("till", f"{year}-{month}-{day}"),
            ("iss.meta", "off"),
            ("iss.json", "extended"),
            ("iss.meta", "off"),
            ("limit", "100"),
            ("start", "0"),
            ("sort_order", "DESC"),
            ("iss.meta", "off"),
            ("iss.json", "extended"),
            ("callback", "JSON_CALLBACK"),
            ("lang", "ru"),
        ]
        api_url = settings.API_URL
        response = requests.get(
            BASE_URL,
            params=params,
        )
        if response.status_code != 200:
            print(response.status_code)
            raise ConnectionError()
        rate = float(response.json()[1].get("securities.current")[0].get("rate"))

        params = {
            "key": "current_rate",
            "value": rate,
        }
        response = requests.patch(
            api_url,
            params=params,
        )
        if response.status_code != 200:
            print(response.status_code)
            raise ConnectionError("Api connection error")
        print(f"curent_rate: {rate}")
        time.sleep(24 * 60 * 60)


if __name__ == "__main__":
    main()
