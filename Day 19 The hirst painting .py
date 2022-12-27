import random
import colorgram as cg
import turtle
turtle.colormode(255)
color_list = [(198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39), (131, 37, 27)]
tim = turtle.Turtle()
screen = turtle.Screen()
tim.penup()
tim.speed("fastest")
x = -200
y = -200
tim.setpos(x,y)

tim.hideturtle()
tim.penup()
for i in range(10):
    for j in range(10):
        tim.dot(20,random.choice(color_list))
        tim.fd(50)
    y+=40
    tim.setpos(x,y)
screen.exitonclick()
