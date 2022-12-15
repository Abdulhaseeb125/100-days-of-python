# Rock ,Paper ,Scissors game.
import random

options = ["rock","paper","scissors"]
player = input("Chose rock , paper or scissors: ").lower()
computer = random.choice(options)

print("player chose : ", player)
print("computer chose :", computer)

if player == computer:
    print("Its draw.")
elif player == "rock" and computer == "paper":
    print("Computer wins.")
elif player == "rock" and computer == "scissors":
    print("Payer wins.")
elif player == "paper" and computer == "rock":
    print("Payer wins.")
elif player == "paper" and computer == "scissors":
    print("Computer wins.")
elif player == "scissors" and computer == "paper":
    print("Payer wins.")
elif player == "scissors" and computer == "rock":
    print("Computer wins.")
else:
    print("invalid player choice, try again")
