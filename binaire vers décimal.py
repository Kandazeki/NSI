numbers = list (input ("Entrez un nombre binaire : "))

coef = 1
n = len(numbers)-1
output = 0

while n >= 0:
    output = output + int(numbers[n]) * coef
    n = n -1
    coef = coef * 2

print ('Bravo !!! Le résultat est ... ', output)
