import html


class Brain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.quiz_list = question_list
        self.current_question = None


    def still_has_questions(self):
        if len(self.quiz_list) != self.question_number:
            return False
        else:
            return True


    def next_question(self):
        self.current_question = self.quiz_list[self.question_number]
        self.question_number += 1
        quiz_question = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {quiz_question}"


    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


