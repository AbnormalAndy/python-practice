from tkinter import Tk, PhotoImage, Canvas, Entry, Button, Label, E, messagebox
from random import choice
import csv
import json

# ---------------------------- CONSTANTS ------------------------------- #

CSV_FILE_PATH='data/french_words.csv'
JSON_FILE_PATH='data/french_words.json'
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Futura"
GREEN = "#9bdeac"
PINK = "#e2979c"
YELLOW = "#f7f5dd"


current_card = {}


# ---------------------------- CONVERT CSV TO JSON ------------------------------- #

def convert_to_json(csvFilePath, jsonFilePath):
    # Create a Dictionary
    json_data = {}


    # Open a CSV reader called DictReader.
    with open(file=csvFilePath, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        json_data = [row for row in csv_reader]


    with open(file=jsonFilePath, mode='w') as json_file:
        json.dump(json_data, json_file)


        # DEBUG
        #print(json_data)


try:
    with open(file='data/french_words.json', mode='r') as data_file:
        french_words = json.load(data_file)


        # DEBUG
        #print(french_words)


except FileNotFoundError:
    convert_to_json(CSV_FILE_PATH, JSON_FILE_PATH)
    with open(file='data/french_words.json', mode='r') as data_file:
        french_words = json.load(data_file)


# ---------------------------- Random Card ------------------------------- # 

def random_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(french_words)
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
    highlightthickness=0, highlightbackground=GREEN, command=random_card)
wrong_button_canvas.grid(column=0, row=1)


# Right Button
right_button_img = PhotoImage(file='images/right.png')
right_button_canvas = Button(image=right_button_img, bg=GREEN,
    highlightthickness=0, highlightbackground=GREEN, command=random_card)
right_button_canvas.grid(column=1, row=1)


random_card()


# Keeps Window Open
window.mainloop()


