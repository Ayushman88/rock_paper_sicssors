import random 

user_win = 0
mac_win = 0

while True:
    print("ROCK~PAPER~SCISSOR Game Welcomes you!")
    
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "Q":
        quit()
        
    if user_input in ["Rock", "Paper", "Scissor"]:
        continue