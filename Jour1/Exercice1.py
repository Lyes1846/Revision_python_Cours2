#Ecrire un programme qui trouve le plus grand nombre  parmi 2 utilisant un prompt

nbr1=input("entrez le premier nombre")
nbr2=input("entrez le deuxieme nombre")
if (nbr1>nbr2):
    print(nbr1+"est plus grand que "+nbr2)
elif(nbr1<nbr2):
    print(nbr2 + "est plus grand que " + nbr1)
else:
    print("les deux  chiffres sont egaux")

    # type casting C'est pour definr ques les 2 nbres sont des entiers
    nbr1 = int(input("entrez le premier nombre"))
    nbr2 = int(input("entrez le deuxieme nombre"))
    #print(type(nbr1),type(nbr2))
if (nbr1 > nbr2):
        print(nbr1 + "est plus grand que " +str(nbr2))
elif (nbr1 < nbr2):
        print(nbr2 + "est plus grand que " +str(nbr1))
else:
        print("les deux  chiffres sont egaux")