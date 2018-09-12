#!/usr/bin/python3
# -*-coding:Utf-8 -*
""" Demarrage du code Labyrinthe - Maze
    Demande si depart de 0 ou sauvegarde 
"""
from SaveInfo import SaveInfo
from WinMaze import WinMaze
import ListMaze

from tkinter import *
from PIL import Image, ImageTk

class WinStart:

    def __init__(self):
        """
        Demarrage du labyrinthe
        Du niveau 0 au niveau 5
        """
        self.win = Tk()
        self.save = None
        self.dessin = Canvas(self.win, width=500, height=500) 
        self.dessin.pack()

        # Image de fond
        fond = Image.open('dk-img/fond.jpg')
        fond = ImageTk.PhotoImage(fond)
        self.dessin.create_image(250,250,image=fond)

        # Nouvelle partie
        start = Button(self.win, text="Nouvelle partie", command=self.start, width = 15)
        self.dessin.create_window(250,200, window = start)

        # Continue partie
        start = Button(self.win, text="Continuer sauvegarde", command=self.cont, width = 15)
        self.dessin.create_window(250,300, window = start)

        self.win.mainloop()

        # Start the game
        level = 0        
        for name_maze in ListMaze.list_Maze:
            # Check the level            
            if self.save.level > level :
                level = level + 1
                continue

            maze = WinMaze(name_maze, (self.save.x , self.save.y ) )

            if maze.trouve == True:
                level = level + 1
                self.save.x = -1
                self.save.y = -1
                self.save.level = level

            else:
                (a,b) = maze.position
                self.save.x = a
                self.save.y = b
                self.save.save()
                maze.maze.save()
                break

    def start(self):
        """ Nouvelle partie """
        self.save = SaveInfo()
        self.save.new()
        self.win.destroy()

    def cont(self):
        """ Partie sauvegardee """
        self.save = SaveInfo()
        self.save.read()
        self.win.destroy()

# Main inclus issu
if __name__ == "__main__" :
    test = WinStart()

