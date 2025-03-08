from tkinter import *
import requests


def get_quote():
    response = requests.get(url='https://stoic.tekloon.net/stoic-quote')
    response.raise_for_status()
    quote = response.json()['data']['quote']
    author = response.json()['data']['author']
    # Used to DEBUG
    #print(quote, author)
    canvas.itemconfig(quote_text,
        text=f'{quote}\n- {author}')


window = Tk()
window.title("Stoice Says...")
window.config(padx=50, pady=50)


canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Stoic Quote Goes HERE", width=250, font=("Futura", 12, "bold"), fill="white")
canvas.grid(row=0, column=0)


bear_img = PhotoImage(file="bear.png")
bear_button = Button(image=bear_img, background='#ffffff', borderwidth=0, highlightthickness=0, command=get_quote)
bear_button.grid(row=1, column=0)


window.mainloop()
