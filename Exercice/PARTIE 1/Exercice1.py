"""
Une fille me dit sur Twitter :

J'aimerais savoir comment s'est possible de détecter si mon nombre de km dépasse mon budget d'essence par mois sur Python !
Budget max : 100€/mois
Kilomètre parcouru : 1053km
Consommation du véhicule : 4.2L/100km)

"""

"""
Info Important à retenir :
SP98 : 1.887€/L -- Nombre à virgule
Budget (par mois): 100€
km_parcouru : 1053km
Consommation : 4.2L/100km == 7.93€/100km
"""

"""
Résultat trouvé sur calculatrice
prix pour 100km = 7.93€
prix_final = 83.50€

Une correction + des idées pour mieux comprendre est dispo sur YT : https://youtu.be/yGK3DB0oYyg

N'OUBLIEZ PAS DE SUPPRIMER LE "PASS" ET DE METTRE À LA PLACE UN PRINT() QUAND VOUS COMMENCEZ À PROGRAMMER
"""

#Créer une fonction qui trouve le prix final et dit celui-ci dépasse son budget ou pas
#Conseil utilisez les fonctions IF & ELSE
#Approfondissement : Afficher le prix final + le budget restant
def prix_conso(prix_essence,budget,km_parcouru,consommation):
    pass


prix_conso(1.887,100,1053,4.2)
