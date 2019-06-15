from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0,10)
    y = randint(0,10)
    op = choice(["+","-","*","/"])
    true_result = 0 
    if op == "+":
        true_result = x + y
    elif op == "-":
        true_result = x - y
    elif op == "*":
        true_result = x * y
    elif op == "/":
        true_result = x/y
    var = randint(-1,1)
    result = true_result + var
    return [x, y, op, result]
    
    #Minh note: Phan return hien thi tren app

def check_answer(x, y, op, result, user_choice):
    if op == "+":
        true_result = x + y
    elif op == "-":
        true_result = x - y
    elif op == "*":
        true_result = x * y
    elif op == "/":
        true_result = x/y
    check = True
    if result == true_result and user_choice == True:
        check = True 
    elif result != true_result and user_choice == False:
        check = True
    else:   
        check = False
    return check
    # pass
# Minh note: return True/False creates sound