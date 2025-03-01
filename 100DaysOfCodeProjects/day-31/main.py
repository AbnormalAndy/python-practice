from tkinter import Tk, PhotoImage, Canvas, Entry, Button, Label, E, messagebox
from random import choice, randint, shuffle
import csv
import json

# ---------------------------- CONSTANTS ------------------------------- #

CSV_FILE_PATH='data/french_words.csv'
JSON_FILE_PATH='data/french_words.json'
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Futura"
GREEN = "#9bdeac"
PINK = "#e2979c"


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


# ---------------------------- UI SETUP ------------------------------- #

# Setup Window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=GREEN)


# Front Card
front_card_img = PhotoImage(file='images/card_front.png')
front_card_canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
front_card_canvas.create_image(400, 263, image=front_card_img)
front_card_language_text = front_card_canvas.create_text(400, 150,
    text='French', font=(FONT_NAME, 40, 'italic'), fill=PINK)
front_card_word_text = front_card_canvas.create_text(400, 263,
    text=f'{french_words[0]['French']}', font=(FONT_NAME, 60, 'bold'), fill=PINK)
front_card_canvas.grid(column=0, row=0, columnspan=2)


# Back Card
# back_card_img = PhotoImage(file='images/card_back.png')
# back_card_canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
# back_card_canvas.create_image(400, 263, image=back_card_img)
#back_card_language_text = back_card_canvas.create_text(400, 150,
#    text='French', font=(FONT_NAME, 40, 'italic'), fill=PINK)
#back_card_word_text = back_card_canvas.create_text(400, 263,
#    text=f'{french_words[0]['English']}', font=(FONT_NAME, 60, 'bold'), fill=PINK)
# back_card_canvas.grid(column=0, row=0, columnspan=2)


# Wrong Button
wrong_button_img = PhotoImage(file='images/wrong.png')
wrong_button_canvas = Canvas(width=100, height=100, bg=GREEN, highlightthickness=0)
wrong_button_canvas.create_image(50, 50, image=wrong_button_img)
wrong_button_canvas.grid(column=0, row=1)


# Right Button
right_button_img = PhotoImage(file='images/right.png')
right_button_canvas = Canvas(width=100, height=100, bg=GREEN, highlightthickness=0)
right_button_canvas.create_image(50, 50, image=right_button_img)
right_button_canvas.grid(column=1, row=1)


# Keeps Window Open
window.mainloop()


