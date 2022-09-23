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





nombre = 511

calc = nombre//2
final = nombre%2

if calc == 0 :
    print (final)

else :
    calc2 = calc//2
    final2 = calc%2

    if calc2 == 0 :
        print (final2, final)

    else :
        calc3 = calc2//2
        final3 = calc2%2

        if calc3 == 0 :
            print (final3, final2, final)

        else :
            calc4 = calc3//2
            final4 = calc3%2

            if calc4 == 0 :
                print (final4, final3, final2, final)

            else :
                calc5 = calc4//2
                final5 = calc4%2

                if calc5 == 0 :
                    print (final5, final4, final3, final2, final)

                else :
                    calc6 = calc5//2
                    final6 = calc5%2

                    if calc6 == 0 :
                        print (final6, final5, fianl4, final3, final2, final)

                    else :
                            calc7 = calc6//2
                            final7 = calc6%2

                            if calc7 == 0 :
                                print (final7, final6, final5, final4, final3, final2, final)

                            else :
                                calc8 = calc7//2
                                final8 = calc7%2

                                if calc8 == 0 :
                                    print (final8, final7, final6, final5, final4, final3, final2, final)

                                else :
                                    calc9 = calc8//2
                                    final9 = calc8%2

                                    if calc9 == 0 :
                                        print (final9, final8, final7, final6, final5, final4, final3, final2, final)

                                    else :
                                        print ("Veuillez entrer un nombre plus petit que 511 s'il vous plait")
        
        




