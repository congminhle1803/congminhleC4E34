# from random import randrange

# n = randrange(0,100)

# i = int(input("Guess my number: "))

# count = 1 

# while i != n:
#     if i>n:
#         print("Too large")
#         i = int(input("Guess my number: "))
#         count += 1 
#     elif i<n:
#         print("Too small")
#         i = int(input("Guess my number: "))
#         count += 1 
#     if count == 7:
#         print("Game over")
#         break
#     if i==n:
#         print("Bingo")
#         break

# Solution (Techkid)

from random import randint

n = randint(0,100)
print(n)
loop = True
count = 0 

while loop:
    answer = int(input("Guess my number? (0-100): "))
    count +=1
    # Count even when just coming into the loop => Save time!
    if answer > n:
        print("Too large")
    elif answer < n:
        print("Too small")
    elif answer == n:
        print("Bingo")
        break

    if count == 7:
        print("Game over!")
        break

# Reason why should not use conditional at while here: complex! While is best to use when do not know exactly times of loop.
# => Set up loop = True => Always run until False or get Break!