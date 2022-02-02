from time import sleep
import liste_mot
from liste_mot import verifie_input
choix_menu = -1
index_liste = 0

print("bienvenue...")

while choix_menu != 0 :
    print("MENU")
    print("1. lecon n°1")
    print("2. lecon n°2")
    print("3. lecon n°3")
    print("4. lecon n°4")
    print("0. Quitter")
    choix_menu = int(input("faites votre choix --->>>"))

    if choix_menu == 1 :

        for texte_a_ecrire in liste_mot.lecon1 :
            print("Recopier le texte ci-desous")
            print(texte_a_ecrire,"\n")
            texte_taper = input("--->>")

            while verifie_input(texte_taper,texte_a_ecrire) == False :
                
                print(texte_a_ecrire,"\n")
                texte_taper = input("--->>")
                verifie_input(texte_taper,texte_a_ecrire)

    elif choix_menu == 2 :

        print("...en chantier....")
        print("-----------------")
        sleep(5)

    elif choix_menu == 3 :

        print("...en chantier....")
        print("-----------------")
        sleep(5)
    elif choix_menu == 3 :

        print("...en chantier....")
        print("-----------------")
        sleep(5)
    elif choix_menu == 4 :

        print("...en chantier....")
        print("-----------------")
        sleep(5)
    else :

        print(" au revoir")



