import requests
from datetime import datetime
from iss import Iss, config
from sun import Sun


payload = {
    "lat": config.MY_LAT,
    "lng": config.MY_LONG,
    "formatted": 0,
}
space_station = Iss()
sun_schedule = Sun(payload)

space_station_at_long = space_station.iss_at_my_long()
space_station_at_lat = space_station.iss_at_my_lat()


sun_set = sun_schedule.is_sun_set()

if sun_set and space_station_at_lat and space_station_at_long:
    print('email sent ISS at Noida')
else:
    print("No email")






#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



