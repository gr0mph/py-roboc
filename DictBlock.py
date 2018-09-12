#!/usr/bin/python3
# -*-coding:Utf-8 -*

from block.StartBlock import StartBlock
from block.WallBlock import WallBlock
from block.OpenGate import OpenGate
from block.CloseGate import CloseGate
from block.FinishBlock import FinishBlock

# For each char, link with a specific Block, inform class/object
dict_Block = {
    "d": StartBlock,
    "m": WallBlock,
    "o": OpenGate,
    "f": CloseGate,
    "a": FinishBlock,
	"-": None
}
