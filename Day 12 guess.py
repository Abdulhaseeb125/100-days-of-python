import random
guesses = 0

def rand_return():
    return random.randint(0, 100)

rand = rand_return()

def Index():
    print(f"i think the number is in between 1 and 100 and it is {rand}")
    print("can you guess it?")
    return input("Chose difficulty level: easy , medium or hard")


def Lives_set():
    level = Index()
    if level == "easy":
        return 10
    elif level == "medium":
        return 7
    elif level == "hard":
        return 5
    else:
        print("invalid command.")
        exit()


guesses = Lives_set()

while guesses >= 0:
    print(f"you have {guesses} lives left")
    if guesses > 0:
        guess = int(input("Guess:"))
    if guess == rand:
        print(f"Good job. You guessed the number {rand}")
        break
    elif guesses == 0:
        print("you run out of lives")
        break
    else:
        if guess > rand:
            print("Too High.")
        elif guess < rand:
            print("Too Low.")
        guesses -= 1

