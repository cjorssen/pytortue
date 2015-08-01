# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:09:50 2015

@author: christophe
"""

import turtle
import time
import numpy as np

turtle.shape("turtle")
turtle.speed("slowest")

avance = turtle.forward
recule = turtle.backward
td = turtle.right
tg = turtle.left

cercle = turtle.circle

dessine = turtle.pendown
ne_dessine_pas = turtle.penup

couleur_feutre = turtle.pencolor
couleur_remplissage = turtle.fillcolor

commence_a_remplir = turtle.fill(True)
finit_de_remplir = turtle.fill(False)

montre_tortue = turtle.showturtle
cache_tortue = turtle.hideturtle

annule = turtle.undo
efface = turtle.clear
recommence = turtle.reset
au_revoir = turtle.bye

turtle.colormode(255)

blanc = (255, 255, 255)
noir = (0, 0, 0)
bleu = (0, 0, 255)
rouge = (255, 0, 0)
vert = (0, 255, 0)
jaune = (255, 255, 0)
magenta = (255, 0, 255)
orange = (255, 165, 0)
cyan = (0, 255, 255)
rose = (255, 192, 203)
