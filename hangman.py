import random
import list as fruits
from stages_assci import *

# default variables
blank_list = []
position = 0
lives = 6

# choosing random word from flist
random_word = random.choice(fruits.wlist)

# creating a blank list of hidden words
for i in random_word:
    blank_list += '_'

# main loop
while '_' in blank_list:

    # input
    guess = input("enter a letter:").lower()
    # checking letter in word loop
    count = 0
    for i in range(len(random_word)):
        if guess == random_word[i]:
            position = i
            count = 1
            blank_list[position] = guess
    # decrementing lives
    # printing in from of list
    print(" ".join(blank_list))
    if count == 0:
        lives -= 1
        print(f"Oh seem like {guess} doesn't exist in word")
        print(stages[lives])
    # number of lives
    print(f"Lives Remaining = {lives}")
    # lives checker
    if lives == 0:
        print("Game Over..... try again")
        print(f"it was '{random_word}'")
        break
    # blank checker
    if not '_' in blank_list:
        print("You win")
