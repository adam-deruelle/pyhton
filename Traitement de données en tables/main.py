import func

#Cle nécessaire au tri
cleEleveId = 'eleve_id'
cleEmail = 'eleve_email'

#Importer les données dans une liste
donnes = func.initalisationCsv("Donnees_Ecole_Danse.csv")


#Récuperer les noms des colonnes concernant les cours
ligneInfoCours = [donnes[0][i] for i in range(5,len(donnes[0]))]

#Mettre les données sous forme de dictionnaires
listDonnesDico = func.convertirListeEnDictionnaire(donnes)
listDonnesDicoTrie = func.trierDictionnaireParSelection(listDonnesDico,cleEleveId)
listEleves = func.supprimerLesDoublons(listDonnesDicoTrie)

#Recuperer les infos sur les cours
listeCours = func.recupererLesValeursDuDictionnaire(listEleves,ligneInfoCours)
listeCours = func.supprimerLesDoublons(listeCours)
listIdCours = func.trierListeParSelection(listeCours)

#Recuperer les mails des eleves du niveau DEBUTANT
listeEmailDebutants = func.recupererLesValeursDuDictionnaire(listEleves,cleEmail)


#Afficher les listes
func.afficherListe(listEleves)
func.afficherListe(listeCours)

