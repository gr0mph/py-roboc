#!/usr/bin/python3
# -*-coding:Utf-8 -*

from block.Block import Block

class FinishBlock(Block):
    """ Finish Block
    L'arrivee du labyrinthe - maze
    """

    abbrevation = "f"
    name = "FinishBlock"
    crossable = True
    symbol = "a"
    image = "arrivee.png"

    def arriver(self):
        """ Remplace la methode check de WinMaze """
        return True

