import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while(1<2):
    print("\n")
    print("Rock,Paper,Scissors - shoot!")
    userChoice= input("your choice [R]ock,[P]aper, or [S]cissors")
    if not re.match("[SsRrPp]", userChoice):
        print ("please choose a letter")
        print ("[R]ock,[P]aper, or [S]cissors")
        continue

    print ("you chose:"+ userChoice)
    choices = ['R','P','S']
    opponentChoice = random.choice(choices)
    print ("I chose: " + opponentChoice)
    if opponentChoice == str.upper(userChoice):
        print ("Tie")
    #elif opponentChoice == str("R") and str.upper(userChoice)=="p"
    elif opponentChoice == 'S' and userChoice.upper() =='P':
        print("scissors beat paper, I win!")
        continue
    elif opponentChoice == 'R' and userChoice.upper() =='S':
        print("rock beats paper, I win")
        continue
    elif opponentChoice == 'P' and userChoice.upper() =='R':
        print("paper beats rock, I win")
        continue
    else:
        print("you win!")
        