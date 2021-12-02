from random import choice
from settings import Settings 
import pygame

class Moves():
    def __init__(self):
        super().__init__()
        self.laban = {
            "Press":"Images/press.bmp",
            "Flick":"Images/flick.bmp",
            "Wring":"Images/wring.bmp",
            "Dab":"Images/dab.bmp",
            "Slash":"Images/slash.bmp",
            "Glide":"Images/glide.bmp",
            "Thrust":"Images/thrust.bmp",
            "Float":"Images/float.bmp",
        }

        self.transitions = {
            "Spin":"Images/spin.bmp",
            "Step":"Images/step.bmp",
        }

        self.s = Settings()
        self.X = self.s.X//2
        self.Y = self.s.Y//2
        self.pos =  "Centerstage center"

    def get_move(self):
        '''Return a random move'''
        self.rand = choice([0,1])
        if self.rand == 0:
            move = choice(list(self.laban.keys()))
        else:
            move = choice(list(self.transitions.keys()))

        return move

    def update(self,new_img):
        self.image = pygame.image.load(new_img)

    def show_move(self, move):
        if self.rand == 0:
            self.image = pygame.image.load(self.laban[move])
        else:
            self.image = pygame.image.load(self.transitions[move])
        self.image = pygame.transform.scale(self.image,(40,40))
        self.img_rect = self.image.get_rect()
        self.img_rect.center = (self.X,self.Y)
        self.s.screen.blit(self.image,self.img_rect) 

    def walk(self):
        if self.rand != 0:
            Xnew = 0
            Ynew = 0
            self.pos = ""
            if self.Y == self.s.Y//6:
                Ynew = choice([0,self.s.Y//3])
                self.pos += "Upstage "
            elif self.Y == self.s.Y//3:
                Ynew = choice([-self.s.Y//3,0,self.s.Y//3])
                self.pos += "Centerstage "
            elif self.Y == self.s.Y//2:
                Ynew = choice([-self.s.Y//3,0])
                self.pos += "Downstage "
            if self.X == self.s.X//6:
                Xnew = choice([0,self.s.X//3])
                self.pos += "left"
            elif self.X == self.s.X//3:
                Xnew = choice([-self.s.X//3,0,self.s.X//3])
                self.pos += "center"
            elif self.X == self.s.X//2:
                Xnew = choice([-self.s.X//3,0])
                self.pos += "right"

            self.X += Xnew
            self.Y += Ynew
            self.s.screen.blit(self.image,self.img_rect)
        return self.pos
