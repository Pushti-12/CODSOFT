import random

items=[1,-1,0]
computer = random.choice(items) #computer will randomly choose from the above list

youstr = input("Enter \n R-Rock \n P-Paper \n S-Scissor:")
youDict = {"R": 1, "P": -1, "S": 0}
reverDict = {1:"Rock" , -1:"Paper", 0:"Scissor"}
you = youDict[youstr]

print(f"computer choosed {reverDict[computer]} and you choosed {reverDict[you]}")

if(computer == you):
    print("it's a draw!")
else:
    #values taken by computer such as -1 and you taken g so value is 0 and computer - you = -1 hence you lose
    if((computer - you) == -1 or (computer - you) == 2): 
        print("you win")
    else:
        print("you lose")