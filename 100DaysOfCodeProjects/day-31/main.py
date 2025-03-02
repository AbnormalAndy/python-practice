from tkinter import Tk, PhotoImage, Canvas, Button
from random import choice
import pandas

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Futura"
GREEN = "#9bdeac"
PINK = "#e2979c"
YELLOW = "#f7f5dd"


current_card = {}
to_learn = {}


try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# ---------------------------- Random Card ------------------------------- # 

def random_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    card_canvas.itemconfig(card, image=front_card_img)
    card_canvas.itemconfig(card_language_text,
        text='French', fill=PINK)
    card_canvas.itemconfig(card_word_text,
        text=f'{current_card['French']}', fill=PINK)
    flip_timer = window.after(3000, flip_card)


# ---------------------------- Flip Card ------------------------------- # 

# Flip Card
def flip_card():
    global current_card
    card_canvas.itemconfig(card, image=back_card_img)    
    card_canvas.itemconfig(card_language_text,
        text='English', fill=YELLOW)
    card_canvas.itemconfig(card_word_text,
        text=f'{current_card['English']}', fill=YELLOW)


# ---------------------------- Create Words to Learn List ------------------------------- # 

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_card()


# ---------------------------- UI SETUP ------------------------------- #

# Setup Window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=GREEN)


# Flip Card
flip_timer = window.after(3000, func=flip_card)


# Card
back_card_img = PhotoImage(file='images/card_back.png')
front_card_img = PhotoImage(file='images/card_front.png')
card_canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
card = card_canvas.create_image(400, 263, image=front_card_img)
card_language_text = card_canvas.create_text(400, 150,
    text='Title', font=(FONT_NAME, 40, 'italic'), fill=PINK)
card_word_text = card_canvas.create_text(400, 263,
    text='Word', font=(FONT_NAME, 60, 'bold'), fill=PINK)
card_canvas.grid(column=0, row=0, columnspan=2)


# Wrong Button
wrong_button_img = PhotoImage(file='images/wrong.png')
wrong_button_canvas = Button(image=wrong_button_img, bg=GREEN,
    highlightthickness=0, highlightbackground=GREEN, command=is_known)
wrong_button_canvas.grid(column=0, row=1)


# Right Button
right_button_img = PhotoImage(file='images/right.png')
right_button_canvas = Button(image=right_button_img, bg=GREEN,
    highlightthickness=0, highlightbackground=GREEN, command=random_card)
right_button_canvas.grid(column=1, row=1)


random_card()


# Keeps Window Open
window.mainloop()


