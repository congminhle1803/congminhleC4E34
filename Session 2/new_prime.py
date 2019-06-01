n = int(input("Please input a number: "))

if n <= 1:
    print("Not prime")

else:
    k= True
    for i in range(2,n-1):
    
        if n%i==0:
            k = False
            break
    if k == False:
        print("Not prime")    
    else: 
        print("Prime")

