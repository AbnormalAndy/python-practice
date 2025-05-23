from data import question_data
from question_model import Question
from quiz_brain import Brain
from ui import QuizInterface


question_bank = []


for i in question_data:
    i = Question(i['question'], i['correct_answer'])
    question_bank.append(i)


brain = Brain(question_bank)
ui = QuizInterface(brain)


print("You have completed the quiz!")
print(f"Final Score: {brain.score}/{brain.question_number}")


