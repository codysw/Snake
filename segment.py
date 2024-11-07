import pygame
import time

from settings import *

class Segment():
    def __init__(self,x,y,size, dir : Direction):
        self.x = x
        self.y = y
        self.size = size
        self.direction = dir

    def get_pos(self):
        return (self.x, self.y)
    
    def move(self, x, y, sets : Settings):
        zeit = sets.zeit

    def add(self, screen, x ,y, sets: Settings):
        self.x = x
        self.y = y
        myRect = pygame.Rect(self.x, self.y,self.size, self.size)
        pygame.draw.rect(screen, (20,20,20), myRect)

    def rm(self, screen, sets : Settings): ### JAKI JA MAM NA TO POMYSL ???
        pass
