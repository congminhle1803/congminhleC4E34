from turtle import *

# speed (0)
shape("turtle")

colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range(len(colors)):
    color(colors[i])
    for k in range(i+3):
        forward(100)
        x = 180 - 180*(i+1)/(i+3)
        left(x)

mainloop()
