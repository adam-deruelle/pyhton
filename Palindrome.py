# Créé par deruelle.a, le 24/09/2021 en Python 3.7
def est_un_palindrome(liste):
    for index in range(len(liste)):
        if liste[index] != liste[-index - 1]:
            return False
        index += 1

    return True

liste_mot = []
str_mot = str(input("Entrer un mot sans accent et sans majuscule: "))
liste_mot = str_mot

if est_un_palindrome(liste_mot):
    print(liste_mot,"est un palindrome")
else:
    print(liste_mot,"n'est pas un palindrome")


