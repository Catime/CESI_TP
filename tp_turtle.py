# -*- coding: utf-8 -*-

from turtle import *
from random import choice

def carre_magique(taille,rotation=90):
    """fonction dessine un carré aléatoire"""
    down()
    liste_couleurs=['Black', 'Red', 'Green', 'Yellow', 'Blue', 'Purple', 'Cyan']
    color(choice(liste_couleurs))
    for k in range(0,4):
        forward(taille)
        left(rotation)
    up()        

if __name__ == '__main__':
    speed("fastest")  
    up()
    goto(-150, 50)
    i = 0
    while i < 10:
        carre_magique(25)
        forward(30)
        i = i +1
    exitonclick()
