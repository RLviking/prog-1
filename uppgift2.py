import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("Rock, paper or scissors? ")

print("The computer chose", computer,"and the user chose", user +".")

# TODO - Implement the if statements that prints who wins
if user == "rock" and computer == "scissors":
    print ("win")

elif user == "paper" and computer == "rock":
    print ("win")

elif user == "scissors" and computer == "paper":
    print ("win")

elif user == computer:
    print ("draw")

else:
    print("lose")

    

