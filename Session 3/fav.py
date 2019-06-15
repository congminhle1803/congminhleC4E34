fav = ["Basket ball", "Thinking", "Business"]

# print("Hello there, here your favorite things")
# print(*fav, sep = ", ")

# new_fav = input("Name one more you wanna add? ")
# fav.append(new_fav)

# print(*fav, sep = ", ")

# for i in range(len(fav)):
#     print(i+1, end = ' . ')
#     print(fav[i])

# Way 2:
for index, value in enumerate(fav):
    print("{0}. {1}".format(index+1 , value))