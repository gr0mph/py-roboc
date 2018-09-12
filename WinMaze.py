#!/usr/bin/python3
# -*-coding:Utf-8 -*
import DictBlock
from ReadMaze import ReadMaze
from block.Block import Block

from tkinter import *
from PIL import Image, ImageTk

class WinMaze:

    def __init__(self, name, position = (-1 , -1)):
        """ Affichage
            Interpretation du fichier labyrinthe - maze
            Deplacement du roboc - Donkey Kong
        """
        self.name = name
        if position == (-1,-1):
            self.maze = ReadMaze(self.name)
        else:
            self.maze = ReadMaze("file-maze/00-tmp-maze.txt")
        self.win = Tk()
        self.icone = []
        self.block = []
        self.position = position
        self.fini = (-1 , -1)
        self.trouve = False

        self.dessin = Canvas(self.win, width=500, height=500) 
        self.dessin.pack()
        
        # Image de fond
        fond = Image.open('dk-img/fond.jpg')
        fond = ImageTk.PhotoImage(fond)
        self.dessin.create_image(250,250,image=fond)

        # Maze ou Labyrinthe
        #print("{}".format(self.position))
        for (a,b) in self.maze :
            x, y = a * 30 + 40 , b * 30 + 40
            block = self.maze.brick((a,b))
            if block :
                #print(block)
                block.open()				
                self.dessin.create_image(x,y,image=block.icone)
                self.dessin.pack()

                # Start position
                if position == (-1,-1) and block.demarrer() :
                    self.position = (a,b)

        # Placer le roboc - Donkey Kong
        self.dk_image("dk_droite.png")
        x, y = self.position
        x, y = x * 30 + 40 , y * 30 + 40
        self.dessin.create_image(x, y, image=self.roboc)

        # Connexion aux clefs
        self.win.bind('<Left>', self.left_key)
        self.win.bind('<Right>', self.right_key)
        self.win.bind('<Up>', self.up_key)
        self.win.bind('<Down>', self.down_key)

        self.win.mainloop()

    def dk_image(self, name):
        """ Specific image pour notre roboc - Donkey Kong """
        self.roboc = Image.open('dk-img/{}'.format(name))
        self.roboc = ImageTk.PhotoImage(self.roboc)

    def move(self):
        """ Deplace Donkey Kong - Roboc """
        x, y = self.position
        x, y = x * 30 + 40 , y * 30 + 40
        self.dessin.create_image(x, y, image=self.roboc)

    def check(self):
        """ Verifie si Donkey Kong est arrive """
        block = self.maze.brick(self.position)
        if block and block.arriver():
            self.trouve = True
            self.win.destroy()

    def left_key(self, event):
        self.dk_image("dk_gauche.png")
        a , b  = self.position
        if a != 0:
            block = self.maze.brick((a-1,b))
            if (not block or block.crossable):
                self.position = (a-1,b)
            elif block.alterable:
                self.maze.replace((a-1,b))
                block = self.maze.brick((a-1,b))
                block.open()				
                x, y = (a-1) * 30 + 40 , b * 30 + 40			
                self.dessin.create_image(x,y,image=block.icone)
                self.dessin.pack()

        self.move()
        self.check()

    def right_key(self, event):
        self.dk_image("dk_droite.png")
        a , b  = self.position
        if a != self.maze.colonne - 1 :
            block = self.maze.brick((a+1,b))
            
            if (not block or block.crossable) :
                self.position = ( a+1 , b )
            elif block.alterable:
                self.maze.replace((a+1,b))
                block = self.maze.brick((a+1,b))
                block.open()				
                x, y = (a+1) * 30 + 40 , b * 30 + 40			
                self.dessin.create_image(x,y,image=block.icone)
                self.dessin.pack()

        self.move()
        self.check()

    def up_key(self, event):
        self.dk_image("dk_haut.png")
        a , b  = self.position
        if b != 0 :
            block = self.maze.brick((a,b-1))

            if (not block or block.crossable):
                self.position = (a,b-1)
            elif block.alterable:
                self.maze.replace((a,b-1))
                block = self.maze.brick((a,b-1))
                block.open()				
                x, y = a * 30 + 40 , (b-1) * 30 + 40			
                self.dessin.create_image(x,y,image=block.icone)
                self.dessin.pack()

        self.move()
        self.check()

    def down_key(self, event):
        self.dk_image("dk_bas.png")
        a , b  = self.position
        if b != self.maze.ligne - 1:
            block = self.maze.brick((a,b+1))

            if (not block or block.crossable):
                self.position = (a,b+1)
            elif block.alterable:
                self.maze.replace((a,b+1))
                block = self.maze.brick((a,b+1))
                block.open()
                x, y = a * 30 + 40 , (b+1) * 30 + 40			
                self.dessin.create_image(x,y,image=block.icone)
                self.dessin.pack()

        self.move()
        self.check()


# Main inclus issu
if __name__ == "__main__" :
    test = WinMaze("file-maze/00-tmp-maze.txt")
    #test = WinMaze("file-maze/01-maze.txt")
    #test = WinMaze("file-maze/02-maze.txt")
    #test = WinMaze("file-maze/03-maze.txt")
    #test = WinMaze("file-maze/04-maze.txt")


