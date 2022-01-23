from datetime import datetime
import requests


def current_date() -> str:
    current_date_time = datetime.now()
    return current_date_time.strftime('%d-%m-%Y')


def current_time() -> str:
    current_date_time = datetime.now()
    return current_date_time.strftime('%H:%M:%S')


def add_row(date: str, time: str, category: str, duration: int, calories: float, url: str, username: str,
            password: str):
    body = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': category,
            'duration': duration,
            'calories': calories
        }
    }

    response = requests.post(url=url, json=body, auth=(username, password))
    print(response.text)
