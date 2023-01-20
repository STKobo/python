import numpy  


# On vous donne une list n, parcourez cette liste et affichez ses valeurs
def display_list(ma_liste: list):
    for i in ma_liste:
        print(i)
    #deuxieme ecriture 
    for i in range(len(ma_liste)):
        print("la valeur est "+ ma_liste[i])
    #troisième ecriture 
    for index, value in enumerate(ma_liste):
        print("la valeur " + value + " est présente à l'index " + index)


#En python, les str sont egalement des tableau. des tableau de caractères
#Avec cette information, afficher chaque lettre d'une phrase donnée en parametre
def display_word_str(un_mot : str):
    for letter in un_mot:
        print(letter)

# Completez la fonction afin qu'elle puisse nous afficher les 100 premiers nombres entiers
def display_hundred_int():
    for i in range(0, 100):
        print(str(i))


# generez des nombres random, ajoutez les dans un tableau et faites la moyenne des notes.
# Si la note, est en dessous de 10 (exclu), affichez "Non admin", sinon, "admin"
def mention_moyenne():
    liste_note : list = []
    for i in range(0, 6):
        liste_note[i] = numpy.random.uniform(0, 20.01)
    somme : float = 0.0
    for i in liste_note: 
        somme += i
    result : float = somme / len(liste_note)
    print("La moyenne des notes est : ", str(result))
        


# Affichez le nombre de voyelle que comporte un mot saisie par l'utilisateur
# Vous pouvez varier cet exercice en affichant le nombre de consonne
def display_number_voyelle():
    print("TODO")


# Affichez la table de multiplication (jusque 10 inclus) d'un nombre saisie par l'utilisateur
# different de 0
def table_multiplication():
    print("TODO")


# Calculez la factorielle d'un nombre
# Pour rappel, la factorielle de 5 vaux (1*2*3*4*5)
def factorielle():
    print("TODO")