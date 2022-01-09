import config
import requests
from datetime import datetime, timezone


class Sun:

    def __init__(self, payload):
        self.response = requests.get(url=config.SUN_API_ENDPOINT, params=payload)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.now = datetime.now(tz=timezone.utc)

    def is_sun_set(self):
        sunset_hr = int(self.data["results"]["sunset"].split("T")[1].split(":")[0])
        sunset_mn = int(self.data["results"]["sunset"].split("T")[1].split(":")[1])

        current_hr = self.now.hour
        current_mn = self.now.minute

        if sunset_hr <= current_hr:
            if sunset_mn < current_mn:
                return True

        return False


