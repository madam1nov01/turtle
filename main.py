from turtle import *
import colorsys

speed(0)
hideturtle()
bgcolor('black')
tracer(5)
width(2)

h = 0.001

for i in range(90):
    color(colorsys.hsv_to_rgb(h, 1, 1))

    forward(100)
    left(60)
    forward(100)
    right(120)
    circle(50)
    left(240)
    forward(100)
    left(60)
    forward(100)

    h += 0.02

    color(colorsys.hsv_to_rgb(h, 1, 1))

    forward(100)
    right(60)
    forward(100)
    left(120)
    circle(-50)
    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)

    h += 0.02

done()
# t.color("red")
# t.speed(10)
# colors = ["red", "blue"]
# for i in range(126):
#     t.forward(30)
#     t.left(10)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(120)
# t.forward(100)

# t.pencolor("red")
# t.color("blue")
# t.speed(1)
