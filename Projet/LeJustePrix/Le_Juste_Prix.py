"""
Ce premier projet est un jeu amusant pour les débutants connu de tous. Le programme génère un prix rond aléatoire. 
Le but pour l’utilisateur est de deviner le prix. 
Chaque fois que l’utilisateur se trompe, l’ordinateur lui dit si c’est plus ou moins que le prix qu’il a donné. 
À chaque aide de l’ordinateur, le score final atteignable par le joueur baisse.

Au programme : 
1- Vous apprendrez à saisir des entrées clavier par un utilisateur
2- Créer des fonctions pour valider que le nombre entré est bien un nombre entier
3- Comparer une variable de référence (le prix) avec une autre variable et de calculer la différence entre deux nombre.
"""
import random
import time

"""
Cette fonction a pour but d'initialiser les premières variables importantes
Le score à 10
Le prix appellera la fonction nb_alea(intervalle) : intervalle étant déjà choisis à partir de la fonction intervalle_prix()
et appellera en fin de fonction game(prix,score,intervalle)
CONSEIL : Le faire à la fin !
"""
def main() :
    #Ajoutez ce qu'il manque
    time.sleep(1)
    print("Le Nombre a été choisi !")
    time.sleep(1)
    print("Passons au jeu !")
    #Ajoutez ce qu'il manque


"""
Cette fonction fonctionnera l'infini jusqu'à ce que le score sera de zéro
pour cela vous utilisez la boucle en while mais aussi des opérateurs logiques.

De plus elle doit faire appel à la fonction nb_joueur(intervalle) qui
fera intervenir le joueur pour choisir un nombre.

Si le joueur trouve a gagné l'afficher sur la console.
CONSEIL : Commencer par faire les fonctions : intervalle_prix() puis nb_joueur(n)
"""
def game(prix,score,intervalle) :
    restart()


"""
Cette fonction a pour but de demander au joueur de choisir un nombre dans une intervalle qu'il choisira.
Elle n'est appellé qu'un fois dans le main()
Ex : il choisit 100, intervalle_prix sortira 100.
Pour faire cela il est OBLIGATOIRE d'utiliser variable = input("Choississez votre intervalle de nombre :").
N'oubliez pas que nous souhaitons une intervalle de type int(entier) ;).

Si le joueur ne choisit pas d'intervalle 3 fois de suite, vous paramétrez l'intervalle à 100.
Vous utilisez la boucle while intervalle==... AND count_error... 3 :

Si c'est le cas, retourner l'intervalle de prix.
"""
def intervalle_prix() :
    pass

"""
La fonction nb_joueur(n) est simillaire à intervalle_prix.
Sauf que celle-ci est appelé des multitudes de fois dans la fonction game(prix,score,intervalle).
Elle a pour but de faire choisir le joueur une valeur entière entre 1 à n(=intervalle_max défini dans intervalle_prix)
N'oubliez pas que le choix du joueur doit être supérieur ou égal à 1 et supérieur ou égal à 1.
Si c'est le cas retourner le choix du joueur
"""
def nb_joueur(n) :
    pass

#Ces 2 derniers programmes n'ont pas besoin d'être touché.

#Le programme nb_alea(n) n'est utilisé qu'une seule fois dans une partie.
#Elle retourne une valeur aléatoire entre 1 à n(comprise)
def nb_alea(n) :
    return random.randint(1,n)

#Cette fonction restart() permet de relancer à volonter le jeu
#En faisant appel au joueur
def restart() :
    restart = input("Voulez-vous recommencer ?(Choix possible : O/N)")
    if restart == "O" : main()
    else : return "Merci d'avoir participé !"

main()