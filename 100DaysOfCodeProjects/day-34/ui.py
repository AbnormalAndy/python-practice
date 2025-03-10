from tkinter import Tk, Canvas, Label, PhotoImage, Button
from quiz_brain import Brain


THEME_COLOR = '#375362'


class QuizInterface:


    def __init__(self, quiz_brain: Brain):
        self.quiz = quiz_brain
        # Window Config
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)


        # Score
        self.score = self.quiz.score
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR,
            font=('Futura', 12))
        self.score_label.grid(column=1, row=0, padx=20, pady=20)


        # Quiz Text
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125,
            text='Quiz Question', width=280, fill='black', font=('Futura', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)


        # True Button
        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, borderwidth=0,
            highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)


        # False Button
        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, borderwidth=0,
            highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)


        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            quiz_question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=quiz_question)
        else:
            self.canvas.itemconfig(self.canvas_text, text='You have reached the end of the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def answer_true(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)
        # Used to DEBUG
        #print(self.quiz.score)


    def answer_false(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)
        #self.score_label.configure(text=f'Score: {self.quiz.score}')
        # Used to DEBUG
        #print(self.quiz.score)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')


        self.score_label.configure(text=f'Score: {self.quiz.score}')

    
        self.window.after(1000, self.get_next_question)


