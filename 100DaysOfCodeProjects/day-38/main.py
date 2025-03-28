import config
import requests


APP_ID = config.APP_ID
API_KEY = config.API_KEY


EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'


exercise_params = {
    'query': 'run for 60 minutes',
    'gender': 'male',
}


exercise_header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0',
}


nutritionix_post_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_header)


nutritionix_post_response.raise_for_status()


print(nutritionix_post_response.text)


