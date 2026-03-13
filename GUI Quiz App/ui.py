from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Display
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", font=FONT, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,width= 275, text="Quiz Question...", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Button Image
        wrong_button_image = PhotoImage(file="./images/false.png")
        correct_button_image = PhotoImage(file="./images/true.png")

        # Button
        self.wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=self.wrong_button)
        self.wrong_button.grid(row=2, column=0)

        self.correct_button = Button(image=correct_button_image, highlightthickness=0, command=self.correct_button)
        self.correct_button.grid(row=2, column= 1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz completed!")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def correct_button(self):
        confirm_answer = self.quiz.check_answer("True")
        self.give_feedback(confirm_answer)

    def wrong_button(self):
        confirm_answer = self.quiz.check_answer("False")
        self.give_feedback(confirm_answer)

    def give_feedback(self, confirm_answer):
        if confirm_answer:
            self.quiz.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)