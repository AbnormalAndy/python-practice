from tkinter import Tk, PhotoImage, Canvas, Entry, Button, Label, E, messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Futura"
RIGHT_JUSTIFY = "e"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    # First delete what is in the password entry field.
    password_entry.delete(0, "end")

    
    letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


    # Randomly chooses a letter, symbol, and then number.
    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]


    # Shuffles password characters.
    shuffle(password_list)


    # Joins the characters into a string from a list.
    password = "".join(password_list)


    # Places generated password in the password entry.
    password_entry.insert(0, password)


    # Debug
    #print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

# Save Information Function
def add_information():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website.lower(): {
            'email': email.lower(),
            'password': password,
        }
    }


    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error",
            message="Please make sure you have not left any fields empty.",
        )


    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data.
                data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)


        else:
            # Updating old data with the new data.
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving updated data.
                json.dump(data, data_file, indent=4)


        finally:
            # Clears entry fields of text.
            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- SEARCH ------------------------------- #

# Find password with website search.
def find_password():
    website_search = website_entry.get().lower()


    test_lowercase = website_search.lower()
    assert test_lowercase == website_search, "Website search not being converted to lowercase."


    try:
        with open("data.json", mode="r") as data_file:
            # Reading old data.
            data = json.load(data_file)


    except FileNotFoundError:
        messagebox.showinfo(
            title="Error",
            message="File NOT found.",
        )


    else:
        try:
            messagebox.showinfo(
                title="Information",
                message=f"Website: {website_search}\n"
                    f"Email: {data[website_search]["email"]}\n"
                    f"Password: {data[website_search]["password"]}",
            )
            print(f"Email: {data[website_search]["email"]}")
            print(f"Password: {data[website_search]["password"]}")


        except KeyError:
            messagebox.showinfo(
                title="Error",
                message="Website NOT found.",
            )


# ---------------------------- UI SETUP ------------------------------- #

# Window Title
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


# Imports Image
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Website Label
website_label = Label(text="Website", font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
website_label.grid(sticky=E, row=1, column=0)


# Website Text Box
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()


# Search Button
search_button = Button(text="Search", font=(FONT_NAME), width=13, command=find_password)
search_button.grid(row=1, column=2)


# Email Label
email_label = Label(text="Email/Username", font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
email_label.grid(sticky=E, row=2, column=0)


# Email Text Box
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)


# Password Label
password_label = Label(text="Password", font=(FONT_NAME), anchor=RIGHT_JUSTIFY)
password_label.grid(sticky=E, row=3, column=0)


# Password Text Box
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# Generate Password Button
generate_password_button = Button(
    text="Generate Password", font=(FONT_NAME), command=generate_password, width=13
)
generate_password_button.grid(row=3, column=2)


# Add Button
add_button = Button(text="Add", font=(FONT_NAME), width=36, command=add_information)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()


