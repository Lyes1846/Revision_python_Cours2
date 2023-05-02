s1="Automatisation des tests "
s2='Tests manuels'
s3="""
Test automatisé 
avec selinium

"""
s4='''
Test automatisé avec RobotFramework
'''
print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))
print (s1)
print (s2)
print (s3)
print (s4)
s5="L'hiver prochain il va faire froid"
s6='cet hiver est "excessivement"froid'

#comment decoupéune chaine de caractere(SLICING)

s1="Automatisation des tests"
print(len(s1))# il y'a 25 caracterres et compris les espaces

#indexation d'une liste
print(s1[0])# le resulata est A, donc c'est la premiere lettre
print(s1[8])
print(s1[13])
print(s1[14])# c'est un espace blanc

#Parcours Inverse
print(s1[-1])
print(s1[-2])
s8=s1+"    "+s2
print(s8)
s9=s1*8
print(s9)#il va ns affiché 8 fois le message s1
