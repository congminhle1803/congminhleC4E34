x = int(input("Input x = "))
y = int(input("Input y = "))
op = input("Input operation (+/-/x/:) ")

result = 0 
alert = 0

if op == "+":
    result = x + y 
elif op == "-":
    result = x - y
elif op == "x":
    result = x*y
elif op == ":":
    if y == 0:
        alert = "Error"
    else:
        result = x/y

if alert == "Error":
    print(alert)
else:
    print("Result = ",result)