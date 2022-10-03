numbers = list(input("Entrez un nombre en base hexadécimal : "))

dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

power = 0
coef = 16
n = len(numbers)-1
output = 0


while n >= 0:
    entry = numbers[n]
    entryInHex = dict[entry]
    output = output + entryInHex*16**power   
    power = power + 1
    n = n - 1

print("le résultat est : ", output)
