import requests


response_trivia = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')


response_trivia.raise_for_status()


question_data = response_trivia.json()['results']


# Used to DEBUG
print(question_data)


