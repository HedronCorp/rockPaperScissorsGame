#Easy part
import random

robotchoice = random.randrange(1,4)
playerchoice = input("choose! (1 - rock 2 - paper  3 - scissors)")

print("Hello user, welcome to the game!")
print("Player 1: ")
print(playerchoice)
print("Player 2: ")
print(robotchoice)

#Hard part
if playerchoice == ("1") and robotchoice == (2):
    print("You Lose!")
if playerchoice == ("2") and robotchoice == (1):
    print("You win!")
if playerchoice == ("3") and robotchoice == (2):
    print("You win!")
if playerchoice == ("1") and robotchoice == (3):
    print("You win!")
if playerchoice == ("2") and robotchoice == (3):
    print("You lose!")
if playerchoice == ("3") and robotchoice == (1):
    print("You win!")
if playerchoice == ("1") and robotchoice == (1):
    print("It's a tie!")
if playerchoice == ("2") and robotchoice == (2):
    print("It's a tie!")
if playerchoice == ("3") and robotchoice == (3):
    print("It's a tie!")
