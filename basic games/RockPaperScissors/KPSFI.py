from random import randint



def finnish():

    #Finnish version
    finnish = ["Kivi", "Paperi", "Sakset"]
    

    name = ""

    if name == "":
        name += input("Pelaajan nimi : ")
        print("jatketaan", name)

        computer = finnish[randint(0,2)] 

    player = input("Kivi, Paperi, Sakset? ")    
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