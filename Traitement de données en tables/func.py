###Ce programme contient les fonctions nécessaire au traitement de données en tables###

#Imports
import csv

#Importe un fichier csv et le rentre dans une liste
def importerCsv(adresseFichier):
    data = []
    with open(adresseFichier, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            data.append(row)
    return data

#Convertit tout les nombres str d'une liste en int
def convertirEnInt(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            estNumerique = data[i][j].isnumeric()
            if estNumerique:
                data[i][j] = int(data[i][j])
    return data

#Importe un fichier csv et le met dans une liste dont les nombres on été converti en int
def initalisationCsv(adresseFichier):
    rowData = importerCsv(adresseFichier)
    data = convertirEnInt(rowData)
    return data
    
#Affiche les éléments de la liste sur plusieurs lignes
def afficherListe(data):
    for element in data:
        print(element)

#Permet de trier par selection une liste contenant des dictionnaires      
def trierDictionnaireParSelection(data,cle):
   for i in range(len(data)):
      # Trouver le min
       indiceMin = i
       for j in range(i+1, len(data)):
           if data[indiceMin][cle] > data[j][cle]:
               indiceMin = j
       data[i],data[indiceMin] = data[indiceMin],data[i] 
   return data

#Permet de trier par selection une liste simple
def trierListeParSelection(data):
   for i in range(len(data)):
      # Trouver le min
       indiceMin = i
       for j in range(i+1, len(data)):
           if data[indiceMin] > data[j]:
               indiceMin = j
       data[i],data[indiceMin] = data[indiceMin],data[i]
       
   return data

#Supprime les éléments en double d'une liste
def supprimerLesDoublons(data):
    listeFinale = []
    for i in range(len(data)-1):
        if data[i] not in listeFinale:
            listeFinale.append(data[i])
    return listeFinale

#Utilise la 1ere ligne de la liste comme clés et le reste comme valeur
def convertirListeEnDictionnaire(data):
    listeFinale = []
    for i in range(1,len(data)-1):
        dictionnaireTemporaire = {}
        for j in range(len(data[i])):
            cle = data[0][j]
            valeur = data[i][j]
            dictionnaireTemporaire[cle]=valeur
        listeFinale.append(dictionnaireTemporaire)
    return listeFinale

#Recupere les valeurs correspondantes à/aux la/les clé(s) donnée(s) des dictionnaires contenu dans une liste
def recupererLesValeursDuDictionnaire(data,cle):
    if type(cle) == str:
        listeValeurs = [data[i][cle]for i in range(len(data))]
    else:
        listeValeurs = []
        for i in range(len(data)):
            ligneTemp = []
            for j in range(len(cle)):
                cleTemporaire = cle[j]
                valeur = data[i][cleTemporaire]
                ligneTemp.append(valeur)
            listeValeurs.append(ligneTemp)
    return listeValeurs

#*args permet de passer un nombre indéfini d'argument (ils seront stocké dans une liste)      
def fusionerListes(*args):
    listeFinale = [*args]
    return listeFinale

#Creer un dictionnaire avec pour valeur une liste
def creerUnDictionnaireValeurListe(cle,valeur):
    dictionnaire = {}
    dictionnaire[cle] = valeur
    return dictionnaire

#Permet de creer les dictionnaires qui ont pour clé les différents attributs des cours
#et pour valeur une liste
def creerUneListeContenantDictionnaire(liste):
    listeFinale = []
    for i in range(len(liste)-1): #Enléve la première ligne qui est celle contenant les clés
        cle = liste[0][i]
        valeur = liste[i+1] #Enléve la première ligne qui est celle contenant les clés
        listeTemp = [creerUnDictionnaireValeurListe(cle,valeur)] 
        listeFinale.append(listeTemp)
    return listeFinale


