#practice of classes and objects
import pygame
screen = pygame.display.set_mode([500,500])


magenta = (255,0,255)
cyan = (0,255,255)
yellow = (255,255,0)

class c():
    def __init__(self,colour,pos,radius,width):
        self.colour = colour
        self.pos = pos
        self.radius = radius
        self.width = width
    

    def draw(self,surface):
        pygame.draw.circle(surface,self.colour,self.pos,self.radius,self.width)

c1 = c(magenta,(250,250),20,0)
c2 = c(cyan,(100,100),35,0)
c3 = c(yellow,(450,450),10,0) #always put class before ur brackets

while True:
    
    screen.fill((255,255,255))
    c1.draw(screen)
    c2.draw(screen)
    c3.draw(screen)
    pygame.display.update()