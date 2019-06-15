from random import shuffle

word = "champion"

letter_list =[]

for i in range(len(word)):
    letter_list.append(word[i])

shuffle(letter_list)

print("List of letters: ", end = '')
print(*letter_list, sep = ', ')

answer = input("Your answer: ")

if answer == word :
    print("Bingo")
else:
    print("Sad")