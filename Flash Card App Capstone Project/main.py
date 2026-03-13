from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

current_card = {}
learning_words = {}

# ---------------------------- READING DATA FROM CSV FILE ------------------------------- #
# Using Pandas
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    learning_words = original_data.to_dict(orient="records")
else:
    learning_words = data.to_dict(orient="records")


# ---------------------------- DISPLAYING THE CARD ------------------------------- #
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learning_words)
    canvas.itemconfig(language_title_text, text="French", fill="black")
    canvas.itemconfig(word_title_text, text=f"{current_card["French"]}", fill="black")
    canvas.itemconfig(card_bg_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(language_title_text, text="English", fill="white")
    canvas.itemconfig(word_title_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg_image, image=card_back_img)


def remove_card():
    learning_words.remove(current_card)
    data = pandas.DataFrame(learning_words)
    data.to_csv("./data/words_to_learn.csv", index=False)
    new_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


# Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_bg_image = canvas.create_image(400, 263, image=card_front_img)

language_title_text = canvas.create_text(400, 150, text="Language", fill="black", font=LANGUAGE_FONT)
word_title_text = canvas.create_text(400, 263, text="Word", fill="black", font=WORD_FONT)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)


# Button Image
wrong_button_image = PhotoImage(file="./images/wrong.png")
right_button_image = PhotoImage(file="./images/right.png")

# Buttons
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_button_image, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

new_card()




window.mainloop()