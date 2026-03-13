from tkinter import *

FONT = ("Times New Roman", 20, "italic")

def miles_to_km():
    miles = float(miles_input.get())   # This method will return the input as a string
    km = round(miles * 1.609)
    calculated_Km_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Creating Label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)

Km_label = Label(text="Km", font=FONT)
Km_label.grid(column=2, row=1)

calculated_Km_label = Label(text="0", font=FONT)
calculated_Km_label.grid(column=1, row=1)

# Button: calls miles_to_km() when pressed
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)





window.mainloop()