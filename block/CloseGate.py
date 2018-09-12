#!/usr/bin/python3
# -*-coding:Utf-8 -*

from block.Block import Block

class CloseGate(Block):
    """ Close Gate Block
    DK est en face d'une porte fermee
    Le block est alterable en une porte ouverte
    """

    abbrevation = "f"
    name = "CloseGate"
    crossable = False
    alterable = "o"
    symbol = "f"
    image = "pf.png"
