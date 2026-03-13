import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ////// get-mouse-click-coordinates-in-python-turtle
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states_data = data["state"]
all_states_list = all_states_data.to_list()
print(all_states_list)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct.",
                                    prompt="Give a state name").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states_list:
        guessed_states.append(answer_state)
        this_state_data = data[data.state == answer_state]
        neon = turtle.Turtle()
        neon.hideturtle()
        neon.penup()
        neon.goto(this_state_data.x.item(), this_state_data.y.item())
        neon.write(answer_state)

remaining_states = []
for states in all_states_list:
    if states not in guessed_states:
        remaining_states.append(states)
    remaining_states_df = pandas.DataFrame(remaining_states)
    remaining_states_df.to_csv("remaining_states.csv")
