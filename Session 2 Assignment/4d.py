n = int(input("Please input n: "))

for i in range(n):
    if i%2==0:
        print("x", end='')
    else:
        print("*", end = '')
