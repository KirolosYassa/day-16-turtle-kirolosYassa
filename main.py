# from turtle import Turtle, Screen
#
# tur = Turtle()
# scr = Screen()
#
# tur.shape("turtle")
# tur.color("red")
# tur.forward(100)
# print(tur)
# print(scr.canvwidth)
# scr.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"


print(table)