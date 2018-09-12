#!/usr/bin/python3
# -*-coding:Utf-8 -*

from tkinter import *
from PIL import Image, ImageTk

class Block:
    """ Classe representant tous les obstacles
    Permet d'alleger le code present dans WinMaze
    Les possibilites seront fournis par appelle de fonction generique presente dans
    cette classe
    """

    abbrevation = "b"
    name = "block"
    crossable = True
    alterable = False
    symbol = ""
    image = ""

    def __init__(self, a, b):
        self.a = a
        self.b = b
        #print(self)

    def demarrer(self):
        """ Permet de trouver le block depart si besoin """
        pass

    def arriver(self):
        """ Remplace la methode check de WinMaze """
        pass

    def open(self):
        self.icone = Image.open('dk-img/{}'.format(self.image))
        self.icone = ImageTk.PhotoImage(self.icone)

    def __repr__(self):
        return "<{} (img={} x={}, y={})>".format(self.name, self.image, self.a, self.b)
