import requests


response = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')


question_data = response.json()['results']

# Used to DEBUG
#print(question_data)


