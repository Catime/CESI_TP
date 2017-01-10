# -*- coding: utf-8 -*-

from turtle import *
from random import choice

def carre_magique(taille,couleur_aleatoire=True):
    down()
    liste_couleurs=['Black','Red','Green','Yellow','Blue','Purple','Cyan']

    if couleur_aleatoire:
        color(choice(liste_couleurs))
    else:
        color(liste_couleurs[0])

    for k in range(0,4):
        forward(taille)
        left(90)
    up()

if __name__ == '__main__':
    speed("fastest")  
    rotation = 15
    taille = 500
    coefficient_rotation = 0.97
    for j in range(0, 150):
      carre_magique(taille,False)
      left(rotation)
      taille = coefficient_rotation*taille
    exitonclick()      

