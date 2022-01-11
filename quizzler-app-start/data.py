import config
import requests


class Data:

    def __init__(self):
        payload = {
            'amount': config.TOTAL_QUESTION,
            'type': config.QUESTION_TYPE
        }
        response = requests.get(url=config.API_END_POINT, params=payload)
        response.raise_for_status()
        self.complete_data = response.json()

    def question_data(self):
        return self.complete_data['results']
