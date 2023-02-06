from random import randint
 


def english():

    #english version
    english = ["Rock", "Paper", "Scissors"]

    #name variable will be empty by default. 
    name="" 

    #player inputs username to make this game a bit more friendly
    if name == "":
        name += input("Name of the player : ")
        print("Lets continue", name)

        #computer selects it's own item
        computer = english[randint(0,2)] 

        #player is asked to choose one of the items
        player = input("Rock, Paper, Scissors? ")

    #winning conditions
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