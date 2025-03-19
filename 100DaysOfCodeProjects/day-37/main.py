import config
import requests


PIXELA_TOKEN = config.PIXELA_TOKEN
PIXELA_USERNAME = config.PIXELA_USERNAME


pixela_endpoint = 'https://pixe.la/v1/users'


params = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
}


requests.post()
