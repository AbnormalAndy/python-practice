import tkinter


# Function to convert miles to kilometers.
def miles_to_km(miles=0):
    miles = float(entry.get())
    km = miles * 1.609
    km_label_two.config(text=f'{km:.2f}', font=('Futura', 12))


# Configuration of window.
window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)


# Takes miles input.
entry = tkinter.Entry(width=10, justify='center')
entry.insert(0, "0")
entry.grid(column=2, row=2)


miles_label = tkinter.Label(text='miles', font=('Futura', 12))
miles_label.grid(column=3, row=2)


km_label_one = tkinter.Label(text='is equal to', font=('Futura', 12))
km_label_one.grid(column=1, row=3)


km_label_two = tkinter.Label(text="0", font=('Future', 12))
km_label_two.grid(column=2, row=3)


km_label_three = tkinter.Label(text='km', font=('Futura', 12))
km_label_three.grid(column=3, row=3)


# Clicking button converts the miles input to kilometers by calling miles_to_km() function.
convert_button = tkinter.Button(text='Calculate', font=('Futura', 12), command=miles_to_km)
convert_button.grid(column=2, row=4)


window.mainloop()


