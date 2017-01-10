# -*- coding: utf-8 -*-

"""
LE JEU du PENDU - V0
© Maxime Souilliart 2017
"""

import string
from random import choice
from tkinter import *

class WinPendu(object):
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.resizable(width=False, height=False)
        self.fenetre.title('Le Pendu - © Maxime Souilliart 2017')
        self.liste_caracteres_autorises = list(string.ascii_lowercase)
        
        self.initialisation_jeu()
        self.interface()
        self.run()

    def initialisation_jeu(self):
        """Initialisation des variables de jeu"""
        self.tentatives = 0
        self.erreurs = 0
        self.max_erreurs = 7
        self.mot_a_trouver = self.mot_aleatoire()
        print(self.mot_a_trouver)
        self.mot_affiche = "?" * len(self.mot_a_trouver)
        self.liste_caractere_utilises = []
        self.boutons = [0]*len(self.liste_caracteres_autorises)


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

    def lettre_clique(self,i):
        lettre = self.liste_caracteres_autorises[i]
        print('lettre clique : %s' % lettre)
        self.liste_caractere_utilises.append(lettre)
        print('Liste des lettres utilisées : %s' % ','.join(self.liste_caractere_utilises) )
        self.boutons[i]['state']='disabled'
        
        if lettre in self.mot_a_trouver:
            for i in range(len(self.mot_a_trouver)):
                if lettre == self.mot_a_trouver[i]:
                    self.supprime_lettres_canevas()
                    self.mot_affiche = self.mot_affiche[:i] + lettre + self.mot_affiche[i+1:]
                    self.ajout_lettres_canevas()
        else:
            self.erreurs+=1
            print('Erreur(s) :  %s/%s' % (self.erreurs,self.max_erreurs))
            if self.erreurs >= self.max_erreurs:
                print('Game Over...')
                print('Le mot caché était : %s' % self.mot_a_trouver )
                                    

    def interface(self):
        self.canevas = Canvas(self.fenetre,bg='ivory', height=400, width=435)
        self.canevas.pack(side=TOP)
        self.ajout_lettres_canevas()

        for i,lettre in enumerate(self.liste_caracteres_autorises):
            self.boutons[i] = Button(self.fenetre, text=lettre,command=lambda x=i:self.lettre_clique(x), height = 1, width = 1)
            self.boutons[i].pack(side=LEFT)

    def run(self):
        self.fenetre.mainloop()

    def ajout_lettres_canevas(self):
        self.canevas_lettres = self.canevas.create_text(320,60,text=self.mot_affiche,fill='black',font='Courrier 40') 

    def supprime_lettres_canevas(self):
        self.canevas.delete(self.canevas_lettres)

    def affichage_mot_canevas(self):
        pass




if __name__ == '__main__':
    winpendu = WinPendu()

