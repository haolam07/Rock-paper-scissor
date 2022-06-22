import random

computerOption = ["Rock", "Paper", "Scissor"]

computerChoice = computerOption[random.randint(0,2)]
print("Welcome to Rock, Paper, Scissor!")
userChoice = input("Enter Rock, Paper, Scissor: ")

computerChoice = computerOption[random.randint(0,2)]
if (computerChoice == "Rock" and userChoice == "Paper" or computerChoice == "Scissor" and userChoice == "Rock" or computerChoice == "Paper" and userChoice == "Scissor"):
  print("You won. I chose " + computerChoice)
elif (computerChoice == "Scissor" and userChoice == "Paper" or computerChoice == "Rock" and userChoice == "Scissor" or computerChoice == "Paper" and userChoice == "Rock"):
  print("You lose. I chose "+ computerChoice)
elif (computerChoice == userChoice):
  print("We tie. I chose " + computerChoice + " too")
print(computerChoice)
