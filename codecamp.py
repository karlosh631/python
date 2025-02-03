import random

def get_choices():
    player_choice =input("Enter a choices (rock, paper, scissors :")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    player = player_choice
    computer = computer_choice
    

def check_win(player , computer):
    print(f"You chose { player}  ,\nComputer chose { computer}")
    if player == "rock" and computer == "scissors":
        return "Player 1 wins"
    elif player == "rock" and computer == "paper":
        return "Computer wins"
    elif computer == "scissors":
        return "Rock smaches scissors ! You won!"
    else:
        return "Paper covers rock. \n You lose!"
    
    
check_win("rock" , "paper ")
 
 
 
 
 


"""
age = 22

if age >=0 and age <=5:
    print("You are a baby.")
elif age >=5 and age <= 17:
    print("You are a kid")
elif age >=25 and age <= 59:
    print("You are an adult") 
else:
    print("You are an old.")
    """