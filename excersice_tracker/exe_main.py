import config
import utility
from nutritionix_api import ExeApi


exercise_text = input('Tell me which exercise you did? ')
nutri_api = ExeApi(api_id=config.API_ID, api_key=config.API_KEY, url=config.exercise_endpoint, query=exercise_text)

activities_list = nutri_api.req_response()['exercises']

current_date = utility.current_date()
current_time = utility.current_time()

for activity in activities_list:
    utility.add_row(date=current_date, time=current_time, category=activity["name"].title(),
                    duration=activity["duration_min"], calories=activity["nf_calories"], url=config.sheet_endpoint,
                    username=config.USERNAME, password=config.PASSWORD)


