#importing random module for ability to randomize computer's choice
import random
winner = ""
#How a "random" choice is selected
randomChoice = random.randint(0,2)
#Assigning the numbers from the random choice into a string so it can be used for a comparison to the user's choice
if randomChoice == 0:
    computerChoice = "Rock"
elif randomChoice == 1:
    computerChoice = "Paper"
else:
    computerChoice = "Scissors"
    
#Prompt to get the user's choice to eventually compare to the computer's choice
userChoice = ""
while (userChoice != "Rock" and
       userChoice != "Paper" and
       userChoice != "Scissors"):
    userChoice = input("Rock, Paper or Scissors")
    
#Comparison and evalution of choices to determine whether the computer wins or the game ends in a tie
if computerChoice == userChoice:
    winner="Tie"
elif computerChoice == "Paper" and userChoice == "Rock":
    winner="Computer"
elif computerChoice == "Rock" and userChoice == "Scissors":
    winner="Computer"
elif computerChoice == "Scissors" and userChoice == "Rock":
    winner="Computer"
else:
    winner="User"
if winner == "Tie":
    print("We both chose", computerChoice + ", play again.")
else:
    print(winner, "won. The computer chose", computerChoice + ".") #Closing satement declaring the winner (or tie) along with the computer's choice
