fav = ["Basket ball", "Thinking", "Business"]

for index, value in enumerate(fav):
    print("{0}. {1}".format(index + 1, value))

i = int(input("Which position do you want to update? "))

update_fav = input("Input your new favorite: ")

fav[i-1] = update_fav

for index, value in enumerate(fav):
    print("{0}. {1}".format(index + 1, value))
