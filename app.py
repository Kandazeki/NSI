number = int(input('Entrez un entier : '))
output = ''

while number > 0:
    remainder = str(number % 2)
    number = number // 2
    output = output + remainder

print ("Résultat en binaire : ", output[::-1])
