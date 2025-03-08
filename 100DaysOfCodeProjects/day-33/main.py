import requests


response = requests.get(url='http://api.open-notify.org/iss-now.json')


response.raise_for_status()


data_latitude = response.json()['iss_position']['latitude']
data_longitude = response.json()['iss_position']['longitude']


print(data_latitude, data_longitude)


