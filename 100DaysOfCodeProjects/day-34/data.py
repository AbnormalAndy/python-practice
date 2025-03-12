import requests


# Gets Data from Website Through API
response_trivia = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')


response_trivia.raise_for_status()


# Transforms Data into JSON
question_data = response_trivia.json()['results']


# Used to DEBUG
#print(question_data)


