from random import randint
import KPSFI as fi
import RPSEN as eng

player = False 

while player == False:

    #player selects language
    print("1. Finnish/Suomi")
    print("2. English/Englanti")
    language = input("select your prefered language : ")
   

    #finnish version see KPSFI file.
    if language == ("1"):
        fi.finnish()
    

    #English version see RPSEN file.
    if language == ("2"):
       eng.english()
    else:
        print("select one of the following languages.")
    player = False