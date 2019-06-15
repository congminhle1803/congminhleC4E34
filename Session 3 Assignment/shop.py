shop = ["T-shirt", "Sweater"]

i = input("Welcome to our shop, what do you want (C, R, U, D)? ")

if i == "R" or i == "r":
    print("Our items: ", end = '')
    print(*shop, sep = ', ')

elif i == "C" or i == "c":
    new_item = input("Enter new item: ")
    shop.append(new_item)
    print("Our items: ", end = '')
    print(*shop, sep = ', ')

elif i == "U" or i == "u":
    position = int(input("Update position: "))
    if position <= len(shop): 
        new_item = input("New item: ")
        shop[position-1] = new_item
        print("Our items: ", end = '')
        print(*shop, sep = ', ')
    else:
        print("Please update in range of shop ({0})".format(len(shop)))

elif i == "D" or i == "d":
    position = int(input("Delete position: "))
    if position <= len(shop):
        del shop[position-1]
        print("Our items: ", end = '')
        print(*shop, sep = ', ')
    else:
        print("Please delete in range of shop ({0})".format(len(shop)))

else:
    print("Please only choose in range (C, R, U, D)")
