import pygame

class Settings:
    def __init__(self):
        self.X = 600
        self.Y = 600

        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.screen = pygame.display.set_mode((self.X,self.Y))

