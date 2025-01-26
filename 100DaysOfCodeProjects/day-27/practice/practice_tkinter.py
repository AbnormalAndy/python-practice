import tkinter


def button_clicked():
    #my_lable.config(text='I clicked the button!')
    my_label.config(text=entry.get())


window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = tkinter.Label(text='I am a Label', font=('Futura', 24, 'bold'))
my_label.pack()


# Button
button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()


# Entry
entry = tkinter.Entry(width=10)
entry.pack()


window.mainloop()


