from tkinter import Tk, Canvas, Label, PhotoImage, Button


THEME_COLOR = '#375362'


class QuizInterface:


    def __init__(self):
        # Window Config
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)


        # Score
        self.score = 0
        self.score_label = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR,
            font=('Futura', 12))
        self.score_label.grid(column=1, row=0, padx=20, pady=20)


        # Quiz Text
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125,
            text='Quiz Question', fill='black', font=('Futura', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)


        # True Button
        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, borderwidth=0,
            highlightthickness=0)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)


        # False Button
        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, borderwidth=0,
            highlightthickness=0)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)


        self.window.mainloop()


