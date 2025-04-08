from datetime import datetime
import config
import requests


# API Configurations
APP_ID = config.APP_ID
API_KEY = config.API_KEY
API_KEY_SHEETY = config.API_KEY_SHEETY


# Endpoints
EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/99857e1bc2a42bffc6f6a39865ac096e/myWorkouts/workouts'


# Today's Date
today = datetime.now()


today_date = today.strftime('%m/%d/%Y')
today_time = today.strftime('%H:%M:%S')


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


nutritionix_post_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_header)
nutritionix_post_response.raise_for_status()
nutritionix_response = nutritionix_post_response.json()


for i in range(len(nutritionix_response['exercises'])):
    sheety_params = {
        'workout': {
            'date': f'{today_date}',
            'time': f'{today_time}',
            'exercise': f'{nutritionix_response['exercises'][i]['user_input'].title()}',
            'duration': f'{nutritionix_response['exercises'][i]['duration_min']}',
            'calories': f'{round(nutritionix_response['exercises'][i]['nf_calories'])}',
        }
    }


    sheety_header = {
        'Authorization': f'Bearer {API_KEY_SHEETY}',
    }


    sheety_post_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_header)
    sheety_post_response.raise_for_status()
    print(sheety_post_response.text)


    #print(nutritionix_response['exercises'][i]['user_input'])
    #print(nutritionix_response['exercises'][i]['duration_min'])
    #print(nutritionix_response['exercises'][i]['nf_calories'])


