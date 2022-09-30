number = int (input ("Entrez un entier décimal : "))
result = ''
remainder = 0

dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

while number > 0 :
    remainder = number % 16

    if remainder >= 10 :
        remainder = dict[remainder]

    number = number // 16
    result = result + str(remainder)

print ("Resultat en hexadecimal : ", result [::-1])

