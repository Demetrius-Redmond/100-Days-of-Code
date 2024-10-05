from tkinter import *

window = Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)




#Label
my_label =Label(text= 'I am a label', font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column= 0, row= )


#Button
def button_clicked():
    print("I got clicked")
    global my_label
    my_label.config(text="Button Got Clicked")

button = Button(text="Click Me", command=button_clicked)
button.grid(column= 1, row= 1)


#New Button
def new_button_clicked():
    print("I got clicked")
    global my_label
    my_label.config(text="New Button Got Clicked")

button = Button(text="New Click Me", command=button_clicked)
button.grid(column= 3, row= 0)


#Entry
input = Entry(width=10)
input.grid(column= 4, row= 3)
input.get()







window.mainloop()