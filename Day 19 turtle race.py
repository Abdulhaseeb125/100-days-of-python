import random
from turtle import Screen, Turtle


screen = Screen()
c_list = ["red", "green", "brown", "orange", "blue", "black", "purple","yellow2"]
screen.setup(height=400, width=600)

turtle_list = []
y = -100
for turtle in range(8):
    turtle_list.append(Turtle("turtle"))
    turtle_list[turtle].color(c_list[turtle])
    turtle_list[turtle].penup()
    turtle_list[turtle].goto(x=-280, y=y)
    y = y + 30
my_turtle = screen.textinput("Turtle color", "Enter color of your turtle").lower()
End = False

while not End:
    for turtle in turtle_list:
        turtle.fd(random.randint(0, 10))
        if turtle.xcor() > 260:
            if turtle.pencolor() == my_turtle:
                print(f"Congratulations.. You Win with color '{turtle.pencolor()}'")
            else:
                print(f"You lose.. Winner is '{turtle.pencolor()}'")
            End = True

screen.exitonclick()
