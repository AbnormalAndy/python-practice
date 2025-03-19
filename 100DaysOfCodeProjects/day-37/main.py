import config
import requests


PIXELA_TOKEN = config.PIXELA_TOKEN
PIXELA_USERNAME = config.PIXELA_USERNAME


pixela_endpoint = 'https://pixe.la/v1/users'
pixela_graph_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs' 


pixela_create_user_params = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}


pixela_graph_config_params = {
    'id': 'graphone',
    'name': 'Drawing Graph',
    'unit': 'minutes',
    'type': 'int',
    'color': 'sora',
}


headers = {
    'X-USER-TOKEN': PIXELA_TOKEN,
}


#pixela_create_user_response = requests.post(url=pixela_endpoint, json=pixela_create_user_params)


pixela_create_graph_response = requests.post(url=pixela_graph_endpoint, json=pixela_graph_config_params, headers=headers)


print(pixela_create_graph_response.text)


