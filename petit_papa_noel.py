# -*- coding: utf-8 -*-

from turtle import *
from random import choice,randrange,uniform

class Sapin(object):

    def __init__(self,x=0,y=0,coef_taille=1):
        self.coef_taille = coef_taille
        up()
        goto(x+8*self.coef_taille,y)
        self.tronc()
        setheading(0)
        goto(x-30*self.coef_taille,y+40*self.coef_taille)
        self.feuillage(100)
        goto(x+20*self.coef_taille,y+150*self.coef_taille)
        self.feuillage(80)
        goto(x+50*self.coef_taille,y+120*self.coef_taille)
        self.feuillage(60)
        goto(x+24*self.coef_taille,y+183*self.coef_taille)
        right(12)
        self.etoile(8*self.coef_taille)

        for i in range(6):
            setposition(x+(randrange(-5,50))*self.coef_taille,y+(randrange(50,75))*self.coef_taille)
            self.boule()

        for i in range(4):
            setposition(x+(randrange(-5,40))*self.coef_taille,y+(randrange(80,120))*self.coef_taille)
            self.boule()

        for i in range(2):
            setposition(x+(randrange(0,30))*self.coef_taille,y+(randrange(120,150))*self.coef_taille)
            self.boule()              
              

    def boule(self):
        setheading(0)
        down()
        liste_couleurs=['Red', 'Yellow', 'Blue', 'Purple', 'Cyan']
        color(choice(liste_couleurs))
        begin_fill()
        circle(4*self.coef_taille)
        end_fill()
        up()

    
    def tronc(self):
        setheading(0)
        down()
        color('brown')
        begin_fill()
        for i in range(1,4):
            if i%2:
                forward(25*self.coef_taille)
            else:
                forward(40*self.coef_taille)
            left(90)
        end_fill()
        up()

    def feuillage(self,taille):
        pencolor("black")
        down()
        color('green')
        begin_fill()
        for i in range(1,3):
            forward(taille*self.coef_taille)
            left(120)
        end_fill()
        up()

    def etoile(self,size):
        pencolor("black")
        angle = 120
        fillcolor("Yellow")
        begin_fill()
        for side in range(5):
            forward(size)
            right(angle)
            forward(size)
            right(72 - angle)
        end_fill()

if __name__ == '__main__':
    speed('fastest')
    bgcolor('#000066')
    hideturtle()

    star_in_sky = []
    for i in range(50):
        up()
        goto(randrange(-300,300),randrange(-300,300))
        down()
        color('white')
        begin_fill()
        circle(randrange(1,2))
        end_fill()
        up()        
               
    pos = [i for i in range(-400,400,50)]
    sapins = [ Sapin(pos[i],-280,uniform(0.2,1.3)) for i in range(15)]
    #s = Sapin(-40,-350,2.4)
    exitonclick()   
