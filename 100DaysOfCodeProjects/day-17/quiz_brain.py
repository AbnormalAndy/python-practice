class Brain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.quiz_list = question_list


    def still_has_questions(self):
        if len(self.quiz_list) != self.question_number:
            return False
        else:
            return True


    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.quiz_list[self.question_number].text} True / False? ")
        self.check_answer(answer, self.quiz_list[self.question_number].answer)
        self.question_number += 1


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That is correct!")
            print(f"Score: {self.score}/{self.question_number + 1}")
        else:
            print("That is wrong!")
            print(f"Score: {self.score}/{self.question_number + 1}")
        print(f"The correct answer: {correct_answer}\n\n")


