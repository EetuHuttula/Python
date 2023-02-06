from random import randint
import KPSFI as fi
import RPSEN as eng

player = False 

while player == False:

    print("1. Finnish/Suomi")
    print("2. English/Englanti")
    language = input("select your prefered language : ")
   

    #finnish version see KPSFI file.
    if language == ("1"):
        fi.finnish()
    

    #English version see RPSEN file.
    else:
       eng.english()

    player = False