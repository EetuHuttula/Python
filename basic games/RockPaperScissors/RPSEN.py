from random import randint
 


def english():

    #english version

    english = ["Rock", "Paper", "Scissors"]

    name="" 

    if name == "":
        name += input("Name of the player : ")
    print("Lets continue", name)
    computer = english[randint(0,2)] 
    player = input("Rock, Paper, Scissors? ")
    if player == computer: 
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print(name, "loses!", computer, "covers", player)
        else:
            print(name, "wins!", player, "breaks", computer)

    elif player == "Paper":
        if computer == "Scissors":
            print(name, "loses!", computer, "cuts", player)
        else:
            print(name, "wins!", player, "covers", computer)

    elif player == "Scissors":
        if computer == "Rock":
            print(name, "loses!", computer, "breaks", player)
        else:
            print(name, "wins!", player, "cuts", computer)   

    else:
        print("Check for spelling mistakes!")  
        return english