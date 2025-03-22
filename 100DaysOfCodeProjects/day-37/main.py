from datetime import date
import config
import requests


# Token and Username Constants
PIXELA_TOKEN = config.PIXELA_TOKEN
PIXELA_USERNAME = config.PIXELA_USERNAME


# Date for Today
today = date.today()


# Pixela Endpoints
pixela_endpoint = 'https://pixe.la/v1/users'
pixela_graph_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs' 
pixela_graph_post_endpoint = f'{pixela_graph_endpoint}/graphone'
pixela_graph_put_endpoint = f'{pixela_graph_endpoint}/graphone/{today.strftime("%Y%m%d")}'


# Pixela Create User Parameters
pixela_create_user_params = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}


# Pixela Graph Config Parameters
pixela_graph_config_params = {
    'id': 'graphone',
    'name': 'Drawing Graph',
    'unit': 'minutes',
    'type': 'int',
    'color': 'sora',
}


# Pixela Graph Post Parameters
pixela_graph_post_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '20',
}


# Pixela Graph Update Parameters
pixela_graph_put_params = {
    'quantity': '0',
}


# Security Header
headers = {
    'X-USER-TOKEN': PIXELA_TOKEN,
}


# Responses from a Post, Put, and Delete Requests
#pixela_create_user_response = requests.post(url=pixela_endpoint, json=pixela_create_user_params)
#pixela_create_graph_response = requests.post(url=pixela_graph_endpoint, json=pixela_graph_config_params, headers=headers)
#pixela_post_to_graph_response = requests.post(url=pixela_graph_post_endpoint, json=pixela_graph_post_params, headers=headers) 
#pixela_put_to_graph_response = requests.put(url=pixela_graph_put_endpoint, json=pixela_graph_put_params, headers=headers) 
pixela_delete_to_graph_response = requests.delete(url=pixela_graph_put_endpoint, headers=headers) 


# Prints Response
print(pixela_delete_to_graph_response.text)


