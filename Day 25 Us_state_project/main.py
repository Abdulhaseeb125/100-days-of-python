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



'''Upadate.........'''



from turtle import Screen, Turtle
import pandas as pd
"""SCREEN SETUP WITH BACKGROUND"""
screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(700, 500)
"""MIAN LOOP"""
Guessed_list = []
df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
while len(Guessed_list) < 50:
    state_input = screen.textinput("State", "Enter the Name:")
    data_list = df[df.state == state_input]
    if state_input == "Exit":
        missing_states = [state for state in all_states if state not in Guessed_list]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missed_data.csv")
        break
    if data_list.empty:
        print("No such state exist.")
    else:
        Guessed_list.append(state_input)
        x = data_list.x
        y = data_list.y
        text = Turtle()
        text.penup()
        text.hideturtle()
        text.goto(x=int(x), y=int(y))
        text.write(f"{state_input}",font=("Arial", 10, "normal"))
screen.exitonclick()

