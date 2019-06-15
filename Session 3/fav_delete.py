fav = ["Basketball", "Thinking", "Business"]

for index, value in enumerate(fav):
    print("{0}. {1}".format(index + 1, value))

i = int(input("Which position do you want to delete? "))

del(fav[i-1])

for index, value in enumerate(fav):
    print("{0}. {1}".format(index + 1, value))
