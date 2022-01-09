import config
import requests


class Iss:

    def __init__(self):
        self.response = requests.get(url=config.ISS_API_ENDPOINT)
        self.response.raise_for_status()
        self.data = self.response.json()

    def iss_at_my_lat(self):
        iss_latitude = float(self.data["iss_position"]["latitude"])
        return iss_latitude == config.MY_LONG

    def iss_at_my_long(self):
        iss_longitude = float(self.data["iss_position"]["longitude"])
        return iss_longitude == config.MY_LONG

