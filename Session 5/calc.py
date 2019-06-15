from random import *
from eval1 import eval

print("Welcome to Freaking Math")

x = randint(0,10)
y = randint(0,10)
op_list = ["+", "-", "*", "/"]

op = choice(op_list)
result = eval(x,y,op)

var = randint(-1,1)
fake_result = result + var

print("{0} {1} {2} = {3}".format(x, op, y, fake_result))

answer = input("Y/N ").upper()
# Using upper to limit conditional

final = 0

if result == fake_result and answer == "Y":
    final = True
elif result == fake_result and answer == "N":
    final = False
elif result != fake_result and answer == "Y":
    final = False
elif result != fake_result and answer == "N":
    final = True

if final == True:
    print("You are right")
else:
    print("You are wrong")


# 2 ways to import:
# (1) from eval1 import eval
# result = eval()

# (2) import eval1
# result = eval1.eval()

