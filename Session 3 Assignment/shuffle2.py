from random import *

word_list = ["venomancer","kunka","sniper","windranger","dazzle","tidehunter","troll","batrider","blood seeker","nevermore","zeus","traxex",
"centaur","storm spirit","shadow shaman", "anti mage","terrorblade","phantom lancer"]

word = word_list[randint(0, len(word_list))]

letter_list = []

for i in range(len(word)):
    letter_list.append(word[i])

shuffle(letter_list)

print("List of letter here: ", end = '')
print(*letter_list, sep = ', ')
print("You have 3 chances!!!")

for i in range(3):
    answer = input("That's a hero in Dota 2. What is your guess? ")
    if answer == word:
        print("Bingo")
        break
    else:
        print("Sad")
        print("You have {0} chances left".format(3-(i+1)))
        