import tkinter


window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)


def button_clicked():
    #my_lable.config(text='I clicked the button!')
    my_label.config(text=input.get())


my_label = tkinter.Label(text='I am a Label', font=('Futura', 24, 'bold'))
my_label.pack()


button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()


input = tkinter.Entry(width=10)
input.pack()


window.mainloop()


