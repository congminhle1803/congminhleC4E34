
#Way 1: length 
# n = input("Please input a number: ")

# print(len(n))

# # Way 2: using loop
# n = int(input("Please input a number: "))

# count = 1 

# while n/10 > 0:
#     count += 1 
#     n = n/10

# print(count)

# Sample solution:

n = int(input("Please input a number: "))

count = 0 

while n > 0:
    n = n//10
    count += 1 
print(count)