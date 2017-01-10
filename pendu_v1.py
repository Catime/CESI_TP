# -*- coding: utf-8 -*-

"""
LE JEU du PENDU - V0
© Maxime Souilliart 2017
"""

from random import choice

class AffichageGraphique(object):
    def titre(self):
        """fonction affichage "titre"""
        print('''                                     
     __            _____              _      
    |  |    ___   |  _  | ___  ___  _| | _ _ 
    |  |__ | -_|  |   __|| -_||   || . || | |
    |_____||___|  |__|   |___||_|_||___||___|
    ''')

    def victoire(self):
        """fonction affichage "gagne"""   
        print('''
       ____       _         ____     _   _     U _____ u       _      _    
    U /"___|u U  /"\  u  U /"___|u  | \ |"|    \| ___"|/     U|"|u  U|"|u  
    \| |  _ /  \/ _ \/   \| |  _ / <|  \| |>    |  _|"       \| |/  \| |/  
     | |_| |   / ___ \    | |_| |  U| |\  |u    | |___        |_|    |_|   
      \____|  /_/   \_\    \____|   |_| \_|     |_____|       (_)    (_)   
      _)(|_    \\    >>    _)(|_    ||   \\,-.  <<   >>       |||_   |||_  
     (__)__)  (__)  (__)  (__)__)   (_")  (_/  (__) (__)     (__)_) (__)_) 
    ''')

    def defaite(self):
        """fonction affichage "game over"""
        print('''
     _____                     _____                
    |   __| ___  _____  ___   |     | _ _  ___  ___ 
    |  |  || .'||     || -_|  |  |  || | || -_||  _|
    |_____||__,||_|_|_||___|  |_____| \_/ |___||_|  
    ''')

    def illustration(self,numeroErreur):
        """fonction affichage erreur en cours"""
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


class Pendu(object):
    def __init__(self):
        self.tentatives = 0
        self.erreurs = 0
        self.max_erreurs = 7
        self.mot_a_trouver = self.mot_aleatoire()
        self.mot_a_trouver_affichage = "*" * len(self.mot_a_trouver)
        self.list_lettres=[]
        self.jeu()

    def mot_urgence(self):
        """cette fonction est utilisée par alimenter le jeu avec un mot alétoire en cas de défaut du fichier texte """
        liste_mots = ['algorithme','saussice','ordinateur','fantastique','python']
        return choice(liste_mots)

    def mot_aleatoire(self):
        """cette fonction sélectionne aléatoirement un mot présent dans le fichier texte liste_mots.txt"""
        try:
            with open("liste_mots.txt", "r") as fichier:
                liste_mots = [ligne.strip() for ligne in fichier]
                mot = choice(liste_mots)
                return mot
        except:
            return self.mot_urgence()

    def score(self):
        return str((len(self.mot_a_trouver)/(self.tentatives+self.erreurs))*100) +" %"

    def jeu(self):
        """FONCTION PRINCIPALE"""
        affichage = AffichageGraphique()
        affichage.titre()
        
        while True:
            self.tentatives +=1
            print('Mot à trouver : %s' % self.mot_a_trouver_affichage )
            
            if len(self.list_lettres)>0:
                print('Liste des lettres utilisées : %s' % ','.join(self.list_lettres) )
            lettre = input('Choississez une lettre :')
            
            if lettre in self.mot_a_trouver and not lettre in self.list_lettres and len(lettre) == 1:
                for i in range(len(self.mot_a_trouver)):
                    if lettre == self.mot_a_trouver[i]:
                        self.mot_a_trouver_affichage = self.mot_a_trouver_affichage[:i] + lettre + self.mot_a_trouver_affichage[i+1:]
            else:
                self.erreurs+=1
                affichage.illustration(self.erreurs)
                print('Erreur(s) :  %s/%s' % (self.erreurs,self.max_erreurs))
                if self.erreurs >= self.max_erreurs:
                    print('')
                    affichage.defaite()
                    print('Le mot caché était : %s' % self.mot_a_trouver )
                    break
                
            if len(lettre) == 1:  
                self.list_lettres.append(lettre)
               
            print('')
            if (self.mot_a_trouver_affichage == self.mot_a_trouver):
                affichage.victoire()
                print('Le mot caché était : %s' % self.mot_a_trouver )
                print('Score : %s' % self.score())
                break


if __name__ == '__main__':
    pendu = Pendu()

