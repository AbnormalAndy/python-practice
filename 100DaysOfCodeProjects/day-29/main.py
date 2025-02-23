from tkinter import Tk, PhotoImage, Canvas, Entry, Button, Label, E, messagebox
from random import choice, randint, shuffle


# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Futura"
RIGHT_JUSTIFY = "e"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


# Save Information Function
def add_information():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    information = f"{website} | {email} | {password}\n"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error",
            message="Please make sure you have not left any fields empty.",
        )

    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: "
            f"\nWebsite: {website}\nEmail: {email}"
            f"\nPassword: {password}\nIs it OK to safe?",
        )

        if is_ok:
            # Writes information to file.
            with open("data.txt", mode="a") as data_file:
                data_file.write(information)

            # Clears entry fields of text.
            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")


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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


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
    text="Generate Password", font=(FONT_NAME), command=generate_password
)
generate_password_button.grid(row=3, column=2)


# Add Button
add_button = Button(text="Add", font=(FONT_NAME), width=36, command=add_information)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
