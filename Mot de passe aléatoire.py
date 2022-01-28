# Créé par deruelle.a, le 22/09/2021 en Python 3.7
from random import *

longueur_mot_de_passe = float(input("Longueur du mot de passe: "))
niveau_de_protection = int(input("Niveau de protection souhaité compris entre 1 et 3: "))
int_longueur_mot_de_passe = int(longueur_mot_de_passe)
str_mot_de_passe = ""
list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_nombres = ['1','2','3','4','5','6','7','8','9']
list_carracter_speciaux = ['&','é','#','è','@','à']



if niveau_de_protection == 1:
    for i in range(int_longueur_mot_de_passe):
        longueur_list_alphabet = len(list_alphabet)
        lettre_aleatoire = list_alphabet[randint(0,longueur_list_alphabet-1)]
        str_mot_de_passe = str_mot_de_passe + lettre_aleatoire

elif niveau_de_protection == 2:
    for i in range(int_longueur_mot_de_passe):
        list_niveau_de_protection_deux = list_alphabet + list_nombres
        longueur_list_niveau_de_proection_deux = len(list_niveau_de_protection_deux)
        lettre_aleatoire = list_niveau_de_protection_deux[randint(0,longueur_list_niveau_de_proection_deux-1)]
        str_mot_de_passe = str_mot_de_passe + lettre_aleatoire

elif niveau_de_protection == 3:
    for i in range(int_longueur_mot_de_passe):
        list_niveau_de_protection_trois = list_alphabet + list_nombres + list_carracter_speciaux
        longueur_list_niveau_de_proection_trois = len(list_niveau_de_protection_trois)
        lettre_aleatoire = list_niveau_de_protection_trois[randint(0,longueur_list_niveau_de_proection_trois-1)]
        str_mot_de_passe = str_mot_de_passe + lettre_aleatoire










print("Votre mot de passe:",str_mot_de_passe)

