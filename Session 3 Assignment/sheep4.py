size = [5, 7, 300, 90, 24, 50, 75]

print("Hello buddy, I'm your fucking dad. Here are my sheep sizes: ")
print(*size, sep = ', ')

max_size = max(size)

print("Now my biggest sheep has size {0} let's shear it".format(max_size))

index = size.index(max_size)

size[index] = 8

print("After shearing, here is my flock: ")
print(*size, sep = ', ')

for i in range(len(size)):
    size[i] += 50

print("One month has passed, now is my flock: ")
print(*size, sep = ', ')