#!/usr/bin/python3
# -*-coding:Utf-8 -*

from block.Block import Block

class OpenGate(Block):
    """ Open Gate Block
    DK est en face d'une porte ouverte
    La porte ouverte est un objet alterable, 
    il peut se transformer en une porte fermee
    (pas utiliser dans le projet)
    """

    abbrevation = "o"
    name = "OpenGate"
    crossable = True
    alterable = "f"    
    symbol = "o"
    image = "po.png"
