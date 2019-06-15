
#list/array

# menu = ["Com", "Chao", "Thit", "Rau", "Dau"]

# index

# print(menu[1])

# print(menu[-1]) #Send back the last value: Dau

# 1. Create
# new_food = "Tom"
# menu.append(new_food)
# print(*menu, sep = ", ")

# 2. Read
# 2.1. Read one
# print(menu[2])

# 2.2. Read many
menu = ["Com", "Chao", "Thit bo", "Rau", "Dau"]
# loop by value
# for food in menu:
#     print(food)

# loop by index
# for i in range(len(menu)):
#     print(i)

# Loop by value & index
# for index, value in enumerate(menu):
#     print(index, value)

# Loop by value & index
# for i in range(len(menu)):
#     print(i, end = ' ')
#     print(menu[i])

# 3. Update
# menu = ["Com", "Chao", "Thit bo", "Rau", "Dau"]
# menu[1] = "Bun"
# print(menu)

# 4. Delete
# menu = ["Com", "Chao", "Thit bo", "Rau", "Dau"]
#delete by index
# del menu[2]

# Delete by value
# menu.remove("Dau")
# print(menu)