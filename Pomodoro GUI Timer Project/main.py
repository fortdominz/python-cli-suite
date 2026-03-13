from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SECS_PER_MIN = 60
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark_label.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_min_in_secs = WORK_MIN * SECS_PER_MIN
    short_break_min_in_secs = SHORT_BREAK_MIN * SECS_PER_MIN
    long_break_min_in_secs = LONG_BREAK_MIN * SECS_PER_MIN

    if REPS % 8 == 0:
        count_down(long_break_min_in_secs)
        title_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_min_in_secs)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_min_in_secs)
        title_label.config(text="Work Timer", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for i in range(work_sessions):
            marks += CHECKMARK
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_Img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_Img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24))
canvas.grid(row=1, column=1)


title_label = Label(text="Timer", font=(FONT_NAME, 20), fg= GREEN, bg=YELLOW)
title_label.grid(row=0, column=1, pady=20)

start_button = Button(text="Start",command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)





window.mainloop()
