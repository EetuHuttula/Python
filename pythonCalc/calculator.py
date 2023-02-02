import mymod as md


while True:
    choice = input("Mitä lasketaan? : ")
    print("Valitse operaatio.")
    print("1. yhteen")
    print("2. Vähennys")
    print("3. kerto")
    print("4. jako")

    if choice in ('1', '2', '3', '4'):
        try: 
            num1 = float(input("Ensimmäinen numero: "))
            num2 = float(input("toinen numero: "))
        except Error:
            print("Numeroita ainoastaan.")
            continue

        if choice == '1':
            print(num1, " + ", num2, " = ", md. add(num1 , num2) )     

        
        elif choice == '2':
            print(num1, " - ", num2, " = ", md.subtract(num1 , num2) )     

       
        elif choice == '3':
            print(num1, " x ", num2, " = ", md.multiply(num1 , num2) )

        
        elif choice == '4':
            print(num1, " / ", num2, " = ", md.divide(num1 , num2) )

    break

