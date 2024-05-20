# Projet: Générateur de mot de passe

# importation des packages nécessaires pour le travail
import random
import string

# Création de la fonction
# Nous allons créer une fonction "generer_mot_de_passe()"

def generer_mot_de_passe():
    
    # Le mot de passe mot contient des lettres, chiffres et symboles
    # ainsi nous assignons chacun des trois à une variable, comme liste.
    lettres = string.ascii_letters
    chiffres = string.digits
    symboles = string.punctuation
    
    # On constitue la liste qui va contenir toutes les variables
    grande_liste = lettres + chiffres + symboles
    
    # Demande d'informations à l'utilisateur
    print("Salut. Ceci est un générateur de mot de passe.")
    print("Veuillez donner les informations requises")
    
    longueur = int(input("Longueur du mot de passe: "))
    nombre_de_mot_de_passe = int(input("Le nombre de mot de passes: "))
    
    # Un mot de passe solide a au moins 8 charactères
    # donc longueur doit être supérieure ou égale à 8
    
    if longueur >= 8:
        print("Mot de passes")
        for i in range(nombre_de_mot_de_passe):
            # Ici on fait passer dans le random.choice la liste "grande_liste"
            # pour qu'il choisisse des éléments de la liste au hazard selon la 
            # la longueur désiré par l'utilisateur
            # la méthode ''.join() est utilisé car random.choice retourne une liste
            # donc avec le ''.join() on crée ainsi une chaine de charactère 
            # à partir des éléments de la liste, créans ainsi le mot de passe.
            mot_de_passe = ''.join(random.choice(grande_liste) for i in range(longueur))
    
            print(mot_de_passe)
    else:
        print("Trop court!!")
        

generer_mot_de_passe()

