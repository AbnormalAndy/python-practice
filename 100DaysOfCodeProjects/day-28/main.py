from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Futura"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- # 



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 



# ---------------------------- UI SETUP ------------------------------- #

# Setup Window
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


# Timer Label
timer_label = Label(text='Timer', font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)


# Check Mark Label
check_label = Label(text='✔', fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=3)


# Tomato Image
tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)


# Start Button
start_button = Button(text='Start', font=(FONT_NAME), highlightbackground=YELLOW)
start_button.grid(column=1, row=3)


# Reset Button
reset_button = Button(text='Reset', font=(FONT_NAME), highlightbackground=YELLOW)
reset_button.grid(column=3, row=3)


window.mainloop()


