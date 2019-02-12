#coding:utf-8
""" c'est une commentaire multiligne """
#une autre commentaire d'un seul ligne

def menu():
    print("----------------------Menu------------------------------")
    print("1-somme\n2-multiplication\n3-division\n4-soustraction\n0-quitter")
    print("----------------------Fin-Menu--------------------------")

compteur=True
while compteur:
    try:
        variable1=int(input("entrez le premiere nombre :"))
        variable2=int(input("entrez le deuxieme nombre :"))
        menu()
        inVariable=int(input("entrez votre choix s'il vous plais :"))
    except:
        print("entrez un numero valide :(")
    if inVariable==1:
        print("la somme de {} + {} = {}".format(variable1,variable2,variable1+variable2))
    elif inVariable==2:
        print("la multiplication de {} * {} = {}".format(variable1,variable2,variable1*variable2))
    elif inVariable==3:
        try:
            print("la division de {} / {} = {}".format(variable1,variable2,variable1/variable2))
        except:
            print("on peut pas diviser sur 0")
    elif inVariable==4:
        print("la soustraction de {} - {} = {}".format(variable1,variable2,variable1-variable2))
    elif inVariable==0:
        print("merci pour utiliser notre calcultrice et à bientôt")
        compteur=False
