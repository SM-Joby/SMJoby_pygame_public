import pygame
pygame.init()
screen = pygame.display.set_mode[(500,500)]

green = (0,255,0)
magenta = (255,0,255)
yellow = (255,255,0)

class rectangle():
    def __init__(self,colour,x,y,length,width):
        self.colour = colour
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.s = screen

    def draw(self):
        pygame.draw.rectangle(self.s,self.colour,(self.x,self.y,self.length,self.width))

    x = 250
    y = 250
    l = 80
    w = 20

    r1 = rectangle(green,(x,y,l,w))
    r2 = rectangle(magenta,(x,y,l,w))
    r3 = rectangle(yellow,(x,y,l,w))

    pygame.display.update()