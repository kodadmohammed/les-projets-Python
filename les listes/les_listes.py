#coding:UTF-8

"""
programme pour gerer les liste juste un exemple pour tester les nouveaux informations
sur python

"""
import pickle
#creation de class Employe
class Employe:
    def __init__(this,nom,prenom,salaire,metier):
        this.nom=nom
        this.prenom=prenom
        this.salaire=salaire
        this.metier=metier
    def afficherEmployer(this):
        print("nom : {}\nprenom : {}\nsalaire : {}\nmetier : {}\n".format(this.nom,this.prenom,this.salaire,this.metier))
        chaine="nom : {}\nprenom : {}\nsalaire : {}\nmetier : {}\n".format(this.nom,this.prenom,this.salaire,this.metier)
        return chaine

#creation de la class Person
class Person:
    compteur_object=0
    def __init__(this,nom):
        this.nom=nom

    def createlistemp(this,liste):
        this.liste=liste

    def menu(this):
        ma_chaine="Menu"
        ma_chaine=ma_chaine.center(50, "-")
        print("{}\n1-ajouter un employer a la liste\n2-supprimer un employer\n3-afficher la liste de employer\n4-enregistrer mes employer dans un fichiers\n5-afficher le contenu de la fichier avnat de quitter\n6-quitter le programme\n".format(ma_chaine))
    def afficherliste(this):
        for p in this.liste:
            print(p.afficherEmployer())


#menu programme

employe1=Employe("mohammed","kodad",1245,"prof")
employe2=Employe("mohammed","kodad",14578,"officier")

listeemp=[employe1,employe2]
person=Person("liste es Employes")
person.createlistemp(listeemp)

#programme
print("bienvenue a notre programme :)\n")
k=True
while k==True:
    person.menu()
    try:
        choix=int(input("\nentrez votre choix s'il vous plais :"))
    except:
        print("une valeur valide")

    if choix==1:
        nom=input("entre le nom d'employee :")
        prenom=input("entre le prenom d'employee :")
        salaire=float(input("entre le salaire d'employee :"))
        metier=input("entre la metier d'employee :")
        person.liste.append(Employe(nom,prenom,salaire,metier))
    elif choix==2:
        person.afficherliste()
        nomsupprimer=input("entrez le nom d'employer a supprimer :) :")
        for p in person.liste:
            if nomsupprimer in p.nom :
                oui_non=input("vous êtes sûr de supprimer l'Employer :{} ".format(nomsupprimer))
                if oui_non=="oui":
                    person.liste.remove(p)
                    print("l'employee a été bien supprimer :)")
                else:
                    print("okay :)")
                break

    elif choix==6:
        k=False
    elif choix==3:
        for p in person.liste:
            print(p.afficherEmployer())
    elif choix==4:
        with open("employe.txt","wb") as fichier:
            for p in person.liste:
                record=pickle.Pickler(fichier)
                chaine=p.afficherEmployer()
                record.dump(chaine)

    elif choix==5:
        with open("employe.txt","rb") as fichier:
            get_record=pickle.Unpickler(fichier)
            get_record=get_record.load()
        print(get_record)




print("\n\n fin de programme...........")
