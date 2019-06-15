# # My solution:
# print('''
# Guess your number game! 
# Now think a number from 0 to 100! 
# All you have to do is to answer:
# If my guess is lower than your number, press 'l'
# If my guess is higher than your number, press 'h'
# If my guess is correct, press 'c'
# ''')

# low = 0
# high = 100

# while True:
#     mid = (low+high)//2
#     print("Is ",mid," is your number? ", end = '')
#     answer = input()
#     if answer == "l":
#         low = mid
#     if answer == "h":
#         high = mid
#     if answer == "c":
#         print("I know it!")
#         break

print('''
# Guess your number game! 
# Now think a number from 0 to 100! 
# All you have to do is to answer:
# If my guess is larger than your number, press 'l'
# If my guess is smaller than your number, press 's'
# If my guess is correct, press 'c'
# ''')

low = 0  
high = 100

while True:
    mid = (low + high)//2
    answer = input("Is {0} your number? ".format(mid))

    if answer == 'l':
        high = mid
    elif answer == 's':
        low = mid
    elif answer == 'c':
        print("I knew it! ")
        break
