from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = 'Futura'
RIGHT_JUSTIFY = 'e'


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
canvas.grid(row=1, column=2)


website_label = Label(text='Website', font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
website_label.grid(sticky = E, row=2, column=1)


website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, columnspan=2)


email_label = Label(text='Email/Username', font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
email_label.grid(sticky = E, row=3, column=1)


email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, columnspan=2)


password_label = Label(text='Password', font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
password_label.grid(sticky = E, row=4, column=1)


password_entry = Entry(width=21)
password_entry.grid(row=4, column=2)


generate_password_button = Button(text='Generate Password', font=(FONT_NAME))
generate_password_button.grid(row=4, column=3)


add_button = Button(text='Add', font=(FONT_NAME), width=36)
add_button.grid(row=5, column=2, columnspan=2)


window.mainloop()


