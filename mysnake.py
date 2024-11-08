import pygame
from enum import Enum
import time

from settings import *
from segment import Segment

class MySnake():
    def __init__(self, sets : Settings):
        self.sets = sets

        x_add = (sets.screen_width/2)%sets.gap
        y_add = (sets.screen_height/2)%sets.gap
        self.x = ( sets.screen_width / 2 ) - x_add
        self.y = ( sets.screen_height / 2 ) - y_add

        self.direction =  Direction.RIGHT
        self.body = [Segment(self.x,self.y,sets.gap,self.direction)]
        self.size = len(self.body) 
        self.rect_size = (sets.gap,sets.gap*self.size)
        
        

    def get_pos(self):
        return (self.x, self.y)

    def eat(self):
        tmp_x = self.body[-1].x          ### SREDNI POMYSL, w skrajnych przypadkach ostatni el moze uciec
        tmp_y = self.body[-1].y          ### przypisuje kierunek poprzedniego
        if self.body[-1].direction == Direction.UP:
            tmp_y += self.sets.gap
        elif self.body[-1].direction == Direction.DOWN:
            tmp_y -= self.sets.gap
        elif self.body[-1].direction == Direction.RIGHT:
            tmp_x -= self.sets.gap
        elif self.body[-1].direction == Direction.LEFT:
            tmp_x += self.sets.gap

        self.body.append( Segment(tmp_x, tmp_y, self.sets.gap, self.body[-1].direction)) 
    def move(self):                 
        sets = Settings()
        zeit = sets.zeit
        time.sleep(zeit)
        if self.direction == Direction.RIGHT:
            time.sleep(zeit)
            for segment in self.body:
                segment.x += self.rect_size[0]
            time.sleep(zeit)
        elif self.direction == Direction.LEFT:
            time.sleep(zeit)
            for segment in self.body:
                segment.x -= self.rect_size[0]
            time.sleep(zeit)
        elif self.direction == Direction.UP:
            time.sleep(zeit)
            for segment in self.body:
                segment.y -= self.rect_size[0]
            time.sleep(zeit)
        elif self.direction == Direction.DOWN:
            time.sleep(zeit)
            for segment in self.body:
                segment.y += self.rect_size[0]
            time.sleep(zeit)

        if self.y >= sets.screen_height:
            self.y = sets.gap
        if self.x >= sets.screen_width:
            self.x = sets.gap
        if self.y < 0:
            self.y = sets.screen_height - (sets.screen_height%sets.gap)
        if self.x < 0:
            self.x = sets.screen_width - (sets.screen_width%sets.gap)
        return
    
    def drawme(self, screen):
        # i = 1
        # copy = self.body[:]
        # while i < len(self.body):
        #     self.body[i].x = copy[i-1].x
        #     self.body[i].y = copy[i-1].y
        #     i += 1
        # self.body[0].x = self.x
        # self.body[0].y = self.y


        for segment in self.body:
            segment.draw( screen, Settings() )

        #screen.fill(self.sets.bg_color)
        #myRect = pygame.Rect(self.x, self.y,self.rect_size[0], self.rect_size[1] )
        #myRect = pygame.Rect( self.size, self.size,self.x, self.y )
        #pygame.draw.rect(screen, (10,10,10), myRect )

    def update(self, screen):
        #print("SNAKE: (", self.x, " , " , self.y , ")" )
        self.move()
        self.drawme(screen)


        
    