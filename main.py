from turtle import Turtle, Screen

tur = Turtle()
scr = Screen()

tur.shape("turtle")
tur.color("red")
tur.forward(100)
print(tur)
print(scr.canvwidth)
scr.exitonclick()