#Name:Devon Black
#Class: 6th Hour
#Assignment: HW17
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def game():
        computer = random.randint(1,3)
        user = int(input("Pick 1 for Rock, Pick 2 for Paper, or Pick 3 for Scissor: "))
        if user == 1:
            print("You picked Rock")
        elif user == 2:
            print("You picked Paper")
        elif user == 3:
            print("You picked Scissor")
        else:
            print("pick a valid number")
            game()
        if computer == 1:
            print("Computer picked Rock")
        elif computer == 2:
            print("Computer picked Paper")
        elif computer == 3:
            print("Computer picked Scissor")
        if user == computer:
            print("Tie!!")
        elif user == 1 and computer == 3 or user == 2 and computer == 1 or user == 3 and computer == 2:
            print("You Win!!")
        else:
            print("You Lose!!")

game()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def playagain():
    while True:
        again = input("Do you want to play again? (y/n): ")
        if again == "y":
            game()
        elif again == "n":
            print("Thank you for playing!")
            break
        else:
            playagain()
playagain()