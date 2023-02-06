from random import randint



def finnish():

    #Finnish version
    finnish = ["Kivi", "Paperi", "Sakset"]
    
    #name variable will be empty by default. 
    name = ""

    #player inputs username to make this game a bit more friendly
    if name == "":
        name += input("Pelaajan nimi : ")
        print("jatketaan", name)

        #computer selects it's own item
        computer = finnish[randint(0,2)] 

    #player is asked to choose one of the items
    player = input("Kivi, Paperi, Sakset? ")

    #winning conditions 
    if player == computer: 
        print("Tasapeli!")

    elif player == "Kivi":
        if computer == "Paperi":
            print(name, "Häviää!", computer, "peittää", player)
        else:
            print(name, "Voittaa", player, "rikkoo", computer)

    elif player == "Paperi":
        if computer == "Sakset":
            print(name, "Häviää!", computer, "leikkaavat", player)
        else:
            print(name, "Voittaa", player, "peittää", computer)

    elif player == "Sakset":
        if computer == "Kivi":
            print(name, "Häviää!", computer, "rikkoo", player)
        else:
            print(name, "Voittaa", player, "leikkaavat", computer)   

    else:
        print("Tarkista kirjoitusvirheet!")
    return finnish       