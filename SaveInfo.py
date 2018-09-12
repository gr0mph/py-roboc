#!/usr/bin/python3
# -*-coding:Utf-8 -*
"""Contient des informations:
- Niveau Labyrinthe
- Emplacement de DK
"""

import json


class SaveInfo:

    def __init__(self):
        self.read()

    def new(self):
        """ Nouvelle partie """
        self.name = "donkey-kong"
        self.level = 0
        self.x = -1
        self.y = -1
        with open("tmp/dk-maze.json", "w") as write_file:
            json.dump(self, write_file, indent=4, default=jdefault)
    
    def save(self):
        """ Sauvegarde """
        with open("tmp/dk-maze.json", "w") as write_file:
            json.dump(self, write_file, indent=4, default=jdefault)

    def read(self):
        """ Lecture """
        try :
            with open("tmp/dk-maze.json", "r") as read_file:
                data = json.load(read_file)
                self.name = data["name"]
                self.level = data["level"]
                self.x = data["x"]
                self.y = data["y"]
        except FileNotFoundError :
            self.name = "donkey-kong"
            self.level = 0
            self.x = -1
            self.y = -1

def jdefault(o):
    return o.__dict__


