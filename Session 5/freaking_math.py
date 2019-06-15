from random import *

print("Welcome to Freaking Math")

x = randint(0,10)
y = randint(0,10)
op_list = ["+", "-", "*", "/"]
# op = op_list[randrange(len(op_list))]
op = choice(op_list)
result = 0

if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x/y

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