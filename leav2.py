"""Définition des classes """
class Classes:
        def __init__(self):
                self.code = 0
                self.titre = "" 
class Eleves:
        def __init__(self):
                self.code = 0
                self.nom = "" 
                self.classe = 0

LReponse = ""

"""Définition des dictionnaires """
eleves = {}
classes = {} 

"""Définition des compteurs"""
Lnombreeleves = 0
Lnombreclasses = 0
Lnumeroeleve = 0
Lnumeroclasse = 0

while LReponse!="0":
	print("********************************************************")
	print("Bienvenue au Lycée d'Excellence d'Abidjan")
	print("********************************************************")
	print("Choisissez une action à mener :")
	print("********************************************************")
	print("1. Enregistrer une classe")
	print("2. Enregistrer un élève")
	print("3. Changer la classe d'un élève")
	print("4. Modifier le nom d'une classe")
	print("5. Modifier le nom d'un élève")
	print("6. Supprimer une classe")
	print("7. Supprimer un élève")
	print("8. Lister les classes")
	print("9. Lister les élèves")
	print("0. Quitter")
	print("********************************************************") 
	LReponse = input("Choisissez une action à mener : ")
	if LReponse == "1":
		print("********************************************************")
		LClasse = input("Entrez le nom de la classe : ")
		Lnumeroclasse += 1
		classes[LClasse] = Classes()
		classes[LClasse].code = Lnumeroclasse
		classes[LClasse].titre = LClasse
	if LReponse == "2":
		print("********************************************************")
		Lnom = input("Entrez le nom et les prénoms de l'élève : ")
		Lnumeroeleve += 1
		print("********************************************************")
		print("Liste des classes enregistrées")
		print("********************************************************")
		for classe in classes.values():
                        print("{0} ".format( classe.titre))
		Lclasse = input("Entrez la classe de l'élève : ")		
		eleves[Lnom] = Eleves()
		eleves[Lnom].code = Lnumeroeleve
		eleves[Lnom].nom = Lnom 
		eleves[Lnom].classe = Lclasse
	if LReponse == "3": 
		print("********************************************************")
		print("Liste des élèves enregistrés")
		print("********************************************************")
		for eleve in eleves.values():
                        print("{0} : {1} ".format( eleve.nom, eleve.classe))
		Leleve = input("Entrez le nom de l'élève : ")
		print("********************************************************")
		print("Liste des classes enregistrées")
		print("********************************************************")
		for classe in classes.values():
                        print("{0} ".format( classe.titre))
		Lclasse = input("Entrez la nouvelle classe de l'élève : ")  
		eleves[Leleve].classe = Lclasse
	if LReponse == "4": 
		print("********************************************************")
		print("Liste des classes enregistrées")
		print("********************************************************")
		for classe in classes.values():
                        print("{0} ".format(classe.titre))
		Lclasse = input("Entrez la classe à modifier : ")
		Lclassenouveau = input("Entrez le nouveau nom de la classe : ")  
		classes[Lclasse].titre = Lclassenouveau
	if LReponse == "5": 
		print("********************************************************")
		print("Liste des élèves enregistrés")
		print("********************************************************")
		for eleve in eleves.values():
                        print("{0} : {1} ".format(eleve.nom, eleve.classe))
		Leleve = input("Entrez l'ancien nom de l'élève à modifier : ")
		Lelevenouveau = input("Entrez le nouveau nom de l'élève : ")
		eleves[Leleve].nom = Lelevenouveau
	if LReponse == "6": 
		print("********************************************************")
		print("Liste des classes enregistrées")
		print("********************************************************")
		for classe in classes.values():
                        print("{0} ".format(classe.titre))
		Lclasse = input("Entrez la classe à supprimer : ")
		del classes[Lclasse]
	if LReponse == "7": 
		print("********************************************************")
		print("Liste des élèves enregistrés")
		print("********************************************************")
		for eleve in eleves.values():
                        print("{0} : {1} ".format(eleve.nom, eleve.classe))
		Leleve = input("Entrez le nom de l'élève à supprimer : ")
		del eleves[Leleve] 
	if LReponse == "8": 
		print("********************************************************")
		print("Liste des classes enregistrées")
		print("********************************************************")
		for classe in classes.values():
                        print("{0}".format(classe.titre))
	if LReponse == "9":
		print("********************************************************") 
		print("Liste des élèves enregistrés")
		print("********************************************************") 
		for eleve in eleves.values():  
                        eleveclasse = eleve.classe
                        classetitre = classes[eleveclasse].titre
                        print("{0} : {1} ".format(eleve.nom, classetitre))
                        
print("********************************************************")                        
print("Le Lycée d'Excellence d'Abidjan (LEA) vous remercie")
print("********************************************************")
print("Aurevoir")
