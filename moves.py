from random import randrange
from settings import Settings 
import pygame

class Moves:
    def __init__(self):
        self.laban = {
            "Press":"Images/press",
            "Flick":"Images/flick",
            "Wring":"Images/wring",
            "Dab":"Images/dab",
            "Slash":"Images/slash",
            "Glide":"Images/glide",
            "Thrust":"Images/thrust",
            "Float":"Images/float",
        }

        self.transitions = {
            "Spin":"Images/spin",
            "Step":"Images/step",
        }
        self.s = Settings()

    def get_move(self):
        '''Return a random move'''
        rand = randrange(0,2)
        if rand == 0:
            rand = randrange(0,len(self.laban))
            move = list(self.laban.keys())[rand]
        else:
            rand = randrange(0,len(self.transitions))
            move = list(self.transitions.keys())[rand]

        return move

