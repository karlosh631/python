import random

def get_choices():
    player_choice =input("Enter a choices (rock, paper, scissors :")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {
        "player": player_choice,
        "computer":computer_choice
        }
    return choices

def check_win(player , computer):
    print(f"You chose { player}  ,\nComputer chose { computer}")
    if player == computer:
        return " its a tie"
    elif player == "rock":
      if computer == "scissors":
        return "Rock smashes scissors ! You won"
    else:
        return  "paper cover rocks ! You lose"
    print ("roxk wins")
  
    
check_win( "rock" , " paper ")