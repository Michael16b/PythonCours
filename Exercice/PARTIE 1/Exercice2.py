"""
Sujet : Import de module interne, Debug, Appel de fonction
Correction + Explication du sujet --> https://youtu.be/TZmfoBFCKPQ
https://youtu.be/-YSoaKdaj7g
"""
import datetime



def main():
    """
    La fonction main() appellera les fonctions :
    1) changement_prenom()
    2) date_naissance()
    tout en les initialisant dans des variables.
    Celle-ci aura pour pour but d'afficher : "Tu t'appelles Lucie et tu es née le 29-01-1995"
    1995 = 27 ans
    """
    pass


def changement_prenom(prenom) :
    #Cette fonction retourne "Lucie"
    pass



def date_naissance(age):
    """
    Cette fonction retourne l'année de naissance d'une personne
    Tips : Veuillez utilisez :
    1) datetime.datetime.now() --> Donne la date d'aujourd'hui
    2)myDatetime.strftime('%Y-%d-%m') --> permet de transformer la date en en chaîne de caractère
    Celui-ci peut-être modifiable à volonter par exemple : myDatetime.strftime('%Y) --> 2022
    """
    pass



print(main())

