from turtle import Screen, Turtle
import pandas as pd
"""SCREEN SETUP WITH BACKGROUND"""
screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(700, 500)
"""MIAN LOOP"""
Ended = False
df = pd.read_csv("50_states.csv")
while not Ended:
    state_input = screen.textinput("State", "Enter the Name:")
    data_list = df[df.state == state_input]
    if state_input == "Exit":
        Ended = True
    elif data_list.empty:
        print("No such state exist.")
    else:
        x = data_list.x
        y = data_list.y
        print(x, y)
        text = Turtle()
        text.penup()
        text.hideturtle()
        text.goto(x=int(x), y=int(y))
        text.write(f"{state_input}",font=("Arial", 10, "normal"))

screen.exitonclick()
