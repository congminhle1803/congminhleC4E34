from turtle import *
from ex5 import draw_star

speed(0)
color('blue')
for i in range(100):
   import random
   x = random.randint(-300, 300)
   y = random.randint(-300, 300)
   length = random.randint(100, 200)
   draw_star(x, y, length)

