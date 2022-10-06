number = (input ("entrez un entier ecrit en base 2, 10 ou 16 : "))

#C'est pour éviter les erreurs

checkNumberArray = list(number)
n = len(checkNumberArray)
i = 0
isError = 0
isBin = 0
isDec = 0

while i < n :
    code = ord(checkNumberArray[i])
    if ((code >= 48 and code <= 57) or (code >= 65 and code <= 70) or (code >= 97 and code <= 102)):
        isError = 0
    else:
        isError = 1
        break
    i = i + 1
    
i = 0
while i < n :
    code = ord(checkNumberArray[i])
    if code >= 48 and code <= 57:
        isDec = 0
    else:
        isDec = 1
        break
    i = i + 1
    
i = 0
while i < n :
    code = ord(checkNumberArray[i])
    if code == 48 or code == 49:
        isBin = 0
    else:
        isBin = 1
        break
    i = i + 1

if isError == 0 :
    if isBin == 1 and isDec == 1:
        base_de_depart = 16
    else:
        base_de_depart = input ("quelle est la base de ce nombre [binaire : 2, décimal : 10 ou Hexadécimal : 16] ? ")

        bases_depart = list(base_de_depart)
        n1 = len(bases_depart)
        i = 0
        isBase = 0
        while i < n1 :
            code = ord(bases_depart[i])
            if code == 49 or code == 50 or code == 48 or code == 54: 
                isBase = 0
            else:
                isBase = 1
                break
            i = i + 1
    
        if isBase == 0 :
            base_de_depart = int(base_de_depart)

if isError == 0 :
    base_darrivee = input ("dans quelle base voulez-vous le convertir [binaire : 2, décimal : 10 ou Hexadécimal : 16] ? ")
        
    bases_darrivee = list(base_darrivee)
    n2 = len(base_darrivee)
    i = 0
    isBaseFinal = 0

    while i < n2 :
        code = ord(bases_darrivee[i])
        if code == 49 or code == 50 or code == 48 or code == 54: 
            isBaseFinal = 0
        else:
            isBaseFinal = 1
            break
        i = i + 1
    if isBaseFinal == 0 :
        base_darrivee = int(base_darrivee)
    
dict_dec_to_hex = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
dict_hex_to_dec = {"0" : 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                   "A":10, "B":11, "C":12, "D":13, "E":14, "F":15,
                   "a":10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}

#C'est les fonctions

def calc_bin_to_dec (number) :
    numbers = list(number)
    coef = 1
    n = len(numbers)-1
    result = 0

    while n >= 0:
        result = result + int(numbers[n]) * coef
        n = n -1
        coef = coef * 2

    return result


def calc_bin_to_hex (number) :
    numbers = list(number)
    coef = 1
    n = len(numbers)-1
    result = 0
    result_hex = ''

    
    while n >= 0:
        result = result + int(numbers[n]) * coef
        n = n -1
        coef = coef * 2

    while result > 0 :
        remainder = result % 16
        if remainder >= 10 :
            remainder = dict_dec_to_hex[remainder]
        result = result // 16
        result_hex = result_hex + str(remainder)
        result_final = result_hex [::-1]

    return result_final 


def calc_dec_to_bin (number) :
    result = ''
    while int(number) > 0 :
        remainder = str(int(number) % 2)
        number = int(number) // 2
        result = result + remainder
    result_final = result [::-1]
    return result_final 


def calc_dec_to_hex (number) :
    result = ''
    remainder = 0
    result_final = ''
    
    while int(number) > 0 :
        remainder = int(number) % 16
        if remainder >= 10 :
            remainder = dict_dec_to_hex[remainder]
        number = int(number) // 16
        result = result + str(remainder)
        result_final = result [::-1]

    return result_final


def calc_hex_to_bin (number) :
    
    numbers = list(number)
    power = 0
    coef = 16
    n = len(numbers)-1
    result = 0

    while n >= 0:
        entry = numbers[n]
        entryInHex = dict_hex_to_dec[entry]
        result = result + entryInHex*16**power   
        power = power + 1
        n = n - 1

    output = ''
    result_final = ''
        
    while result > 0:
        remainder = str(result % 2)
        result = result // 2
        output = output + remainder
        result_final = output [::-1]
        
    return result_final        


def calc_hex_to_dec (number) :
    
    numbers = list(number)
    power = 0
    coef = 16
    n = len(numbers)-1
    result = 0
    
    while n >= 0:
        entry = numbers[n]
        entryInHex = dict_hex_to_dec [entry]
        result = result + entryInHex * 16 ** power   
        power = power + 1
        n = n - 1
        
    return result

#Le programme principal

if isError == 0:
    if base_de_depart == 2 :
        if isBin == 0 :
            if base_darrivee == 2 :
                    result = number
                    print ("le résultat est : ", result)

            elif base_darrivee == 10 :
                print ('Bravo !!! Le resultat en décimal est ... ', calc_bin_to_dec(number))

            elif base_darrivee == 16 :
        
                print ("Resultat en hexadecimal : ", calc_bin_to_hex(number))

            else:
                print ("veuillez entrer une base valide (2, 10 ou 16)")

        else :
            print ("Ce n'est pas un binaire") 

    elif base_de_depart == 10 :
        if isDec == 0 :
            if base_darrivee == 10 :
                result = number
                print ("le resultat est : ", result)

            elif base_darrivee == 2 :
                print ("Resultat en binaire : ", calc_dec_to_bin(number))

            elif base_darrivee == 16 :
                print ("Resultat en hexadecimal : ", calc_dec_to_hex (number))

            else :
                print ("veuillez entrer une base valide (2, 10 ou 16)")
        else :
            print ("Ce n'est pas un décimal")

    elif base_de_depart == 16 :

        if base_darrivee == 16 :
            result = number
            print ("le resultat est : ", result)

        elif base_darrivee == 2 :
            print ("Resultat en binaire : ", calc_hex_to_bin(number))


        elif base_darrivee == 10 :
            print("le résultat est : ", calc_hex_to_dec (number))

        else :
            print ("Veuillez entrer une base valide (2, 10 ou 16)")

    else :
        print ("Votre base de depart n'est pas valide, choisissez un nombre en base 2, 10 ou 16")
else:
    print ('ERROR ! Nous ne pouvons pas convertir cela...')
