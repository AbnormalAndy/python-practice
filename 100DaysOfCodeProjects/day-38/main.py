import config
import requests


APP_ID = config.APP_ID
API_KEY = config.API_KEY
API_KEY_SHEETY = config.API_KEY_SHEETY


EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/99857e1bc2a42bffc6f6a39865ac096e/myWorkouts/workouts'


# Input for exercise.
exercise = input('Tell me which exercises you did: ')


# Nutritionix Params
exercise_params = {
    'query': exercise,
    'gender': 'female',
    'weight_kg': 58.97,
    'height_cm': 162.56,
    'age': 30,
}


# Nutritionix Header Information
exercise_header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0',
}


sheety_params = {
    'workout': {
        'date': 'meowdate',
        'time': 'meowtime',
        'exercise': 'meowexercise',
        'duration': 'meowduration',
        'calories': 'meowcalories',
    }
}


sheety_header = {
    'Authorization': f'Bearer {API_KEY_SHEETY}',
}


#nutritionix_post_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_header)
#nutritionix_post_response.raise_for_status()
#print(nutritionix_post_response.text)


#sheety_get_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_header)
#sheety_get_response.raise_for_status()
#print(sheety_get_response.text)


sheety_post_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_header)
sheety_post_response.raise_for_status()
print(sheety_post_response.text)


