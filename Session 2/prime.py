# Kiem tra so nguyen to 

n = int(input("Please input a number: "))

# i == 2
count = 1
for i in range(2,n):
    if n%i==0:
        count = count + 1
        print("Not prime")
        break
if count == 1 :
    print("Prime")

# Dung bien ao de kiem tra.
# Dung break de ket thuc vong lap.


        