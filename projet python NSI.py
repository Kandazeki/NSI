nombre = int (input ("entrez un entier écrit en base 2, 10 ou 16 : "))

base_de_depart = (input ("quelle est la base de ce nombre ? "))

base_darrivee = (input ("dans quelle base voulez-vous le passer ? "))


nombre_final (nombre, base_de_depart, base_darrivee)
if base_de_depart == 2 :
    if base_darrivee == 2 :
            nombre_final == nombre

    if base_darrivee == 10 :
            nombre_final == int ('base_de_depart',10)

    if base_darrivee == 16 :
        nombre_final == int ('base_de_depart',16)

    else :
        print ("veuillez entrer une base valide (2, 10 ou 16)")

if base_de_depart == 10 :
    if base_darrivee == 10 :
        nombre_final == nombre

    if base_darrivee == 2 :
        nombre_final == int ('base_de_depart',2)

    if base_darrivee == 16 :
        nombre_final == int ('base_de_depart',16)

    else :
        print ("veuillez entrer une base valide (2, 10 ou 16)")

if base_de_depart == 16 :
    if base_darrivee == 16 :
        nombre_final == nombre

    if base_darrivee == 2 :
        nombre_final == int ('base_de_depart',2)

    if base_darrivee == 10 :
        nombre_final == int ('base_de_depart',10)

    else :
        print ("Veuillez entrer une base valide (2, 10 ou 16)")

else :
    print ("Votre base de départ n'est pas valide, choisissez un nombre en base 2, 10 ou 16")

print (nombre_final)

