from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #

# Window Title
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


# Imports Image
logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.pack()


window.mainloop()


