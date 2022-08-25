tab = [1,2,3,4,5,6,7]


#Parcourir un tableau par itération sans lien avec la table
def tab1() :
    for  i in range(7) :
        print(tab[i])

#Parcourir un tableau par itération avec un lien  avec la table
def tab2() :
    for i in range(len(tab)) :
        print(tab[i])

#Parcourir un tableau par valeur
def tab3(): 
    for value in tab :
        print(value)
#tab1()
#tab2()
#tab3()
        


#La fonction recherche, recherche la valeur v(par exemple 7) dans un tableau
#Si c'est le cas elle retourne True
#Sinon False
def recherche(tab,v) :
    pass

#print(recherche(tab,7)) # --> True
#print(recherche(tab,8))  # --> False
#print(recherche(tab,17))  # --> False
#print(recherche(tab,2)) # --> True


#Bonus
#La fonction recherche2, recherche la valeur v(par exemple 7) dans un tableau
#Si c'est le cas elle retourne l'index
#Sinon -1
def recherche2(tab,v) :
    pass


#print(recherche2(tab,7)) # --> 6
#print(recherche2(tab,8))  # --> -1
#print(recherche2(tab,17))  # --> -1
#print(recherche2(tab,2)) # --> 1








tab2 = [10,12,15,20,30]


#Ajout de valeur
def tab_ajout(tab2,v) :
    tab2.append(v)
    return tab2

#tab_ajout(tab2,7)
#print(tab2)


#Suppression de valeur par itération
def tab_suppr1(tab2,i) :
    del tab2[i]
    return  tab2

#print(tab_suppr1(tab2,1))
#print(tab_suppr1(tab2,-1))


#Suppresion de valeur sur une intervalle donnée
def tab_suppr2(tab2,i,v) :
    del tab2[i:v]
    return  tab2

#print(tab_suppr2(tab2,1,3))



#tab2 = [10,12,15,20,30]

def value_tab_move(tab2,i,v) :
    tab2[i],tab2[v] = tab2[v], tab2[i] 
    return tab2


#print(value_tab_move(tab2,1,3))

def value_tab_move1(tab2,i,v) :
    s = tab2[i]
    tab2[i]= tab2[v]
    tab2[v] = s
    return tab2

#print(value_tab_move1(tab2,1,3))


#Nous avons ce tableau pris en paramètre : [0,15,20,35,10,35,40,38]
#Et on souhaite trouver ce tableau(de façon la plus optimisé): [15,40,35,38,70]
#Vous n'avez le droit d'utilisez qu'une seule fois chaque fonction vu précedemment(pour optimiser le programme)
#Vous appellerez les fonctions vu précedemment
#TIPS : La fonction doit faire 5 lignes
def modif_table(tab3) :
    tab3 = tab_suppr1(tab3,0)
    tab3 = tab_suppr2(tab3,1,4)
    tab3 = tab_ajout(tab3,70)
    tab3 = value_tab_move(tab3,1,2)
    return tab3

print(modif_table([0,15,20,35,10,35,40,38]))
