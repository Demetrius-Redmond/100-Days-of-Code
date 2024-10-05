from tkinter import *


window = Tk()
window.title("Mile to Km Converter")

window.config(padx=25, pady=25)

#Entry
input = Entry(width=5)
input.grid(column= 1, row= 0)
input.get()


#Label
miles_label =Label(text= 'Miles', font=("Arial", 12, "bold"))
miles_label.grid(column= 2, row= 0)


#Label
equal_label =Label(text= 'is equal to', font=("Arial", 12, "bold"))
equal_label.grid(column= 0, row= 1)


#Label
output_label =Label(text= '0', font=("Arial", 12, "bold"))
output_label.grid(column= 1, row= 1)


#Label
km_label =Label(text= 'Km', font=("Arial", 12, "bold"))
km_label.grid(column= 2, row= 1)


#Button
def calculate():
    miles = float(input.get())
    km = 0
    km = miles * 1.6
    output_label.config(text=f"{km}")

button = Button(text="Calculate", command=calculate)
button.grid(column= 1, row= 2)



















window.mainloop()