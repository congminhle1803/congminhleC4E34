from turtle import *

speed(0)

color("red")

shape("turtle")

right(30)

for k in range (4):
    for i in range(2):
        forward(100)
        left(60)
        forward(100)
        left(120)
    right(90)

mainloop()