import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])

red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
screen.fill((255,255,255))#always use two sets of brackets

class c():
    def __init__(self):
        self.color = red 
        self.radius = 20
        self.pos = 250,250
        self.width = 0
        self.s = screen
    
    def draw(self):
        pygame.draw.circle(self.s,self.color,self.radius, self.pos,self.width)

c1 = c(screen,red,20,(250,250),0)

class r():
    def __init__(self):
        self.colour = green
        self.x = 24
        self.y = 255
        self.length = 80
        self.width = 40
        self.s = screen
    
    def draw(self):
        pygame.draw.rect(self.s,self.colour,self.x,self.y,self.length,self.width)
    
r1 = r(screen,green,(24,255),80,40)

class l():
    def __init__(self):
        self.colour = yellow
        self.pos = 80,300
        self.length = 100
        self.s = screen

    def draw(self):
        pygame.draw.line(self.s, self.color, self.pos,self.length)
    
l1 = l(yellow,(80,300),100)

pygame.display.update()

