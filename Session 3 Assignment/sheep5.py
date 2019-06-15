size = [5, 7, 300, 90, 24, 50, 75]

print("Hello buddy, I'm your fucking dad. Here are my sheep sizes: ")
print(*size, sep = ', ')
month = int(input("How many months do you want to grow sheeps? "))

for i in range(month):
    print("MONTH {0}".format(i+1))
    for k in range(len(size)):
        size[k] += 50
    print("One month has passed. Here is my flock now: ")
    print(*size, sep = ', ')

    # max_size = max(size)
    print("Now my biggest sheep has size {0}. Let's shear it".format(max(size)))

    index_max = size.index(max(size))
    size[index_max] = 8
    print("After shearing, here is my flock: ")
    print(*size, sep = ', ')
    
# total = 0
# for i in range(len(size)):
#     total = total + size[i]
# print("My flock has size in total: ", total)
# print("I would get: {0} * 2$ = {1}$".format(total))

