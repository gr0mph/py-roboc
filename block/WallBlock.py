#!/usr/bin/python3
# -*-coding:Utf-8 -*

from block.Block import Block

class WallBlock(Block):
    """ Wall Block
    DK est en face d'un mur
    Il ne peut pas traverser
    """

    abbrevation = "m"
    name = "WallBlock"
    crossable = False
    symbol = "m"
    image = "mur.png"
