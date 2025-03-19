import config
import requests


PIXELA_TOKEN = config.PIXELA_TOKEN
PIXELA_USERNAME = config.PIXELA_USERNAME


pixela_endpoint = 'https://pixe.la/v1/users'


pixela_user_params = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}


#pixela_create_user_response = requests.post(url=pixela_endpoint, json=pixela_user_params)


