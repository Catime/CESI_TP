# -*- coding: utf-8 -*-

"""
LE JEU du PENDU - V0
© Maxime Souilliart 2017
"""

from random import choice

def titre():
    """
    fonction affichage "titre"
    """       
    print('''                                         
 __            _____              _      
|  |    ___   |  _  | ___  ___  _| | _ _ 
|  |__ | -_|  |   __|| -_||   || . || | |
|_____||___|  |__|   |___||_|_||___||___|
''')

def victoire():
    """
    fonction affichage "gagne"
    """    
    print('''
   ____       _         ____     _   _     U _____ u       _      _    
U /"___|u U  /"\  u  U /"___|u  | \ |"|    \| ___"|/     U|"|u  U|"|u  
\| |  _ /  \/ _ \/   \| |  _ / <|  \| |>    |  _|"       \| |/  \| |/  
 | |_| |   / ___ \    | |_| |  U| |\  |u    | |___        |_|    |_|   
  \____|  /_/   \_\    \____|   |_| \_|     |_____|       (_)    (_)   
  _)(|_    \\    >>    _)(|_    ||   \\,-.  <<   >>       |||_   |||_  
 (__)__)  (__)  (__)  (__)__)   (_")  (_/  (__) (__)     (__)_) (__)_) 
''')

def defaite():
    """
    fonction affichage "game over"
    """
    print('''
 _____                     _____                
|   __| ___  _____  ___   |     | _ _  ___  ___ 
|  |  || .'||     || -_|  |  |  || | || -_||  _|
|_____||__,||_|_|_||___|  |_____| \_/ |___||_|  
''')

def illustration(numeroErreur):
    """
    fonction affichage erreur en cours
    """
    pict = ["""""",
"""
---------
 |     |
 |
 |
 |
 |
 |""",
 """
 ---------
 |     |
 |     o
 |
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |    -+-
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |    |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |    | |
 |
 |"""]
    print(pict[numeroErreur])

def mot_urgence():
    """
    cette fonction est utilisée par alimenter le jeu avec un mot alétoire en cas de défaut du fichier texte 
    """
    liste_mots = ['algorithme','saussice','ordinateur','fantastique','python']
    return choice(liste_mots)

def mot_aleatoire():
    """
    cette fonction sélectionne aléatoirement un mot présent dans le fichier texte liste_mots.txt
    """
    try:
        fichier = open("liste_mots.txt", "r")
        liste_mots = [ligne.strip() for ligne in fichier]
        mot = choice(liste_mots)
        return mot
    except:
        return mot_urgence()


def main():
    """
    FONCTION MAIN
    """
    titre()
    tentatives = 0
    erreur = 0
    max_erreurs = 7
    mot_a_trouver = mot_aleatoire()
    mot_a_trouver_affichage  = "*" * len(mot_a_trouver)
    list_lettres=[]

    while True:
        
        tentatives +=1
        print('Mot à trouver : %s' % mot_a_trouver_affichage )
        
        if len(list_lettres)>0:
            print('Liste des lettres utilisées : %s' % ','.join(list_lettres) )
        lettre = input('Choississez une lettre :')
        
        if lettre in mot_a_trouver and not lettre in list_lettres and len(lettre) == 1:
            for i in range(len(mot_a_trouver)):
                if lettre == mot_a_trouver[i]:
                    mot_a_trouver_affichage = mot_a_trouver_affichage[:i] + lettre + mot_a_trouver_affichage[i+1:]
        else:
            erreur+=1
            illustration(erreur)
            print('Erreur(s) :  %s/%s' % (erreur,max_erreurs))
            if erreur >= max_erreurs:
                print('')
                defaite()
                print('Le mot caché était : %s' % mot_a_trouver )
                break
            
        if len(lettre) == 1:  
            list_lettres.append(lettre)
           
        print('')
        if (mot_a_trouver_affichage == mot_a_trouver):
            victoire()
            print('Le mot caché était : %s' % mot_a_trouver )
            print('Tentatives : %s' % tentatives )
            print('erreur :  %s' % erreur )
            break


if __name__ == '__main__':
    main()

