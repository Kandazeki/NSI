number = (input ("entrez un entier ecrit en base 2, 10 ou 16 : "))

base_de_depart = int (input ("quelle est la base de ce nombre [binaire : 2, décimal : 10 ou Hexadécimal : 16] ? "))

base_darrivee = int (input ("dans quelle base voulez-vous le convertir [binaire : 2, décimal : 10 ou Hexadécimal : 16] ? "))



if base_de_depart == 2 :

    if base_darrivee == 2 :
            result = number
            print ("le résultat est : ", result)

    elif base_darrivee == 10 :
        numbers = list(number)
        coef = 1
        n = len(numbers)-1
        result = 0

        while n >= 0:
            result = result + int(numbers[n]) * coef
            n = n -1
            coef = coef * 2
        print ('Bravo !!! Le resultat en décimal est ... ', result)

    elif base_darrivee == 16 :
        numbers = list(number)
        coef = 1
        n = len(numbers)-1
        result = 0

        while n >= 0:
            result = result + int(numbers[n]) * coef
            n = n -1
            coef = coef * 2

        result_hex = ''
        remainder = 0

        dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

        while result > 0 :
            remainder = result % 16

            if remainder >= 10 :
                remainder = dict[remainder]

            result = result // 16
            result_hex = result_hex + str(remainder)

        print ("Resultat en hexadecimal : ", result_hex [::-1])


    else:
        print ("veuillez entrer une base valide (2, 10 ou 16)")


elif base_de_depart == 10 :
    
    if base_darrivee == 10 :
        result = number
        print ("le resultat est : ", result)

    elif base_darrivee == 2 :
        result = ''

        while int(number) > 0:
            remainder = str(int(number) % 2)
            number = int(number) // 2
            result = result + remainder

        print ("Resultat en binaire : ", result[::-1])

    elif base_darrivee == 16 :
        result = ''
        remainder = 0

        dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

        while int(number) > 0 :
            remainder = int(number) % 16

            if remainder >= 10 :
                remainder = dict[remainder]

            number = int(number) // 16
            result = result + str(remainder)

        print ("Resultat en hexadecimal : ", result [::-1])

    else :
        print ("veuillez entrer une base valide (2, 10 ou 16)")

elif base_de_depart == 16 :
    
    if base_darrivee == 16 :
        result = number
        print ("le resultat est : ", result)

    elif base_darrivee == 2 :
        numbers = list(number)

        dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

        power = 0
        coef = 16
        n = len(numbers)-1
        result = 0


        while n >= 0:
            entry = numbers[n]
            entryInHex = dict[entry]
            result = result + entryInHex*16**power   
            power = power + 1
            n = n - 1

        output = ''

        while result > 0:
            remainder = str(result % 2)
            result = result // 2
            output = output + remainder

        print ("Resultat en binaire : ", output[::-1])


    elif base_darrivee == 10 :
        numbers = list(number)

        dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

        power = 0
        coef = 16
        n = len(numbers)-1
        result = 0


        while n >= 0:
            entry = numbers[n]
            entryInHex = dict[entry]
            result = result + entryInHex*16**power   
            power = power + 1
            n = n - 1

        print("le résultat est : ", result)

    else :
        print ("Veuillez entrer une base valide (2, 10 ou 16)")

else :
    print ("Votre base de depart n'est pas valide, choisissez un nombre en base 2, 10 ou 16")

