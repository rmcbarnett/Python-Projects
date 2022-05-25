from tkinter import *

def button_clicked():
    miles = int(miles_input.get())
    km = round(miles * 1.60934,2)
    km_answer_label["text"] = str(km)



window = Tk()
window.title("Miles to Km Converter")
window.minsize(500,300)
window.config(padx=100,pady=50)

# my_label = Label()
# my_label["text"] = "test"
# my_label.grid(column=0, row = 0)
# my_label.config(padx = 20, pady=20)


miles_input = Entry(width = 10)
miles_input.grid(column=1, row = 0)


mile_label = Label()
mile_label["text"] = "Miles"
mile_label.grid(column=2, row = 0)
mile_label.config(padx= 20, pady=20)

is_equal_label = Label()
is_equal_label["text"] = "is equal to"
is_equal_label.grid(column=0, row = 1)
is_equal_label.config(padx= 20)

km_answer_label = Label()
km_answer_label["text"] = ""
km_answer_label.grid(column=1, row = 1)
km_answer_label.config(padx= 20)

km_label = Label()
km_label ["text"] = "Km"
km_label.grid(column=2, row = 1)
km_label .config(padx= 20)

button=Button(text="Calculate", command=button_clicked)
button.grid(column=1, row = 3)


window.mainloop()
