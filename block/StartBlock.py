#!/usr/bin/python3
# -*-coding:Utf-8 -*

from block.Block import Block

class StartBlock(Block):
    """ Starting Block
    Where DK starting his maze
    """

    abbrevation = "d"
    name = "StartingBlock"
    crossable = True
    symbol = "d"
    image = "depart.png"

    def demarrer(self):
        """
        Ainsi la classe ReadMaze est informee que DK peut commencer ici
        """
        return True

