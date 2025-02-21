from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = 'Futura'
RIGHT_JUSTIFY = 'e'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_information():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    information = f'{website} | {email} | {password}\n'
    

    # Writes information to file.
    with open(f'data.txt', mode='a') as file:
        file.write(information)


    # Clears entry fields of text.
    website_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

# Window Title
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


# Imports Image
logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Website Label
website_label = Label(text='Website', font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
website_label.grid(sticky = E, row=1, column=0)


# Website Text Box
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


# Email Label
email_label = Label(text='Email/Username', font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
email_label.grid(sticky = E, row=2, column=0)


# Email Text Box
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)


# Password Label
password_label = Label(text='Password', font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
password_label.grid(sticky = E, row=3, column=0)


# Password Text Box
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# Generate Password Button
generate_password_button = Button(text='Generate Password', font=(FONT_NAME))
generate_password_button.grid(row=3, column=2)


# Add Button
add_button = Button(text='Add', font=(FONT_NAME), width=36, command=add_information)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()


