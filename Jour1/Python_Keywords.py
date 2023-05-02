#Retrouvez les mots reservés de python(KeyWords)
import keyword

import keyword


print(keyword.kwlist)
print(len(keyword.kwlist))
a=25
#on ne peut pas nommer Les identifiant (variables) avec les keywords
#Exemple as=25 ou import=25 (as et import=keywords )
#123somme=25  Les identifiants ne commencent pas par un nombre
somme123=25   #ca c'est correcte
#somme$=25
# un identifiant ne peut pas contenir un caractère spécial.
somme=25
_somme=25
  #les identifiants peuvent contenir un underscore