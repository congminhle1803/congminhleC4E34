size = [5, 7, 300, 90, 24, 50, 75]

print("Hello buddy, I'm your fucking dad. Here are my sheep sizes: ")
print(*size, sep = ', ')

max_size = 0

for value in size:
    if value > max_size:
        max_size = value     

# max_size = max(size)

print("Now my biggest sheep has size {0} let's shear it".format(max_size))

