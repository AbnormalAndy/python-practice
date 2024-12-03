from data import question_data
from question_model import Question


question_bank = []


for i in question_data:
    i = Question(i['text'], i['answer'])
    question_bank.append(i)


print(question_bank)


