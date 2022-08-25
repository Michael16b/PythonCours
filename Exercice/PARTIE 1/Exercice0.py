"""
Aujourd'hui, vous allez apprendre à créer vos additions, soustractions et multiplication
"""



def addition() :
    #Créer une addition qui permet de trouver la valeur 8.
    # Si celle-ci est bonne alors la fonction ne devrait pas retourner des erreurs(type AssertionError)
    maPremiereVariable = 4
    maDeuxiemeVariable = 4
    assert(maPremiereVariable+maDeuxiemeVariable == 8)
    return str(maPremiereVariable) + " + " + str(maDeuxiemeVariable) + " est bien égal à 8."

#print(addition()) #Enlever le "#" à côté du print pour faire fonctionner votre fonction

def soustraction() :
    # Idem que la première
    maPremiereVariable = 0
    maDeuxiemeVariable = 0
    assert(maPremiereVariable-maDeuxiemeVariable == -17)
    return str(maPremiereVariable) + " - " + str(maDeuxiemeVariable) + " est bien égal à -17."

#print(soustraction()) 

def multiplication() :
    # Idem que la première
    maPremiereVariable = 0
    maDeuxiemeVariable = 0
    assert(maPremiereVariable*maDeuxiemeVariable == 35)
    return str(maPremiereVariable) + " - " + str(maDeuxiemeVariable) + " est bien égal à 35."


#print(multiplication())






