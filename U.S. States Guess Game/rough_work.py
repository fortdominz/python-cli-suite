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

answer_state = input("Enter answer: ").title()
data = pandas.read_csv("50_states.csv")
states_data = data["state"]
states_list = states_data.to_list()
print(states_list)

if answer_state in states_list:
    print(answer_state)






