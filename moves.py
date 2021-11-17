from random import choice
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
            move = choice(list(self.laban.keys()))
        else:
            move = choice(list(self.transitions.keys()))

        return move

    def show_move(self, move, screen):
        image = pygame.image.load(laban[move])
        img_rect = image.get_rect()
        

    def walk(self):


