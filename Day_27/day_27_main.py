from tkinter import *

window = Tk()
window.title('Miles to KM Convertor')
window.minsize(width=300, height=100)

# Entry

entry = Entry(window, width=10, bd=2)
entry.insert(index=END, string=0)
entry.grid(column=1, row=0)

# Miles Label

miles_label = Label(window, text='Miles')
miles_label.grid(column=2, row=0)

# equal to Label

eq_label = Label(window, text='is equal to', pady=20)
eq_label.grid(column=0, row=1)

# actual KM

a_km_label = Label(window, text='0', pady=20)
a_km_label.grid(column=1, row=1)

# KM

km_label = Label(window, text='KM', pady=20)
km_label.grid(column=2, row=1)


# calculate button

def miles_to_km():
    miles = float(entry.get())
    km = round(miles * 1.61, 0)
    a_km_label.config(text=km)


calculate_btn = Button(window, text='Calculate', command=miles_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()
