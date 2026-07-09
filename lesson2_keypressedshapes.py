import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])

red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)

class c():
    def __init__(self,colour,pos,radius,width):
        self.colour = colour
        self.pos = pos
        self.radius = radius
        self.width = width

    def draw(self,surface):
        pygame.draw.circle(surface,self.colour,self.pos,self.radius,self.width)

c1 = c(red,(250,250),20,0)
screen.fill((255,255,255))

class r():
    def __init__(self,colour,x,y,length,width):
        self.colour = colour
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        
    def draw(self,surface):
        pygame.draw.rect(surface,self.colour,(self.x,self.y,self.length,self.width))

r1 = r(blue,100,100,60,40)
screen.fill((255,255,255))

class l():
    def __init__(self,colour,s,e):
        self.colour = colour
        self.s = s
        self.e = e

    def draw(self,surface):
        pygame.draw.line(surface,self.colour,self.s,self.e)

l1 = l(yellow,(350,350),(450,450))
screen.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill((255,255,255))
                c1.draw(screen)
                pygame.display.update()
            elif event.key == pygame.K_r:
                screen.fill((255,255,255))
                r1.draw(screen)
                pygame.display.update()
            elif event.key == pygame.K_l:
                screen.fill((255,255,255))
                l1.draw(screen)
                pygame.display.update()
    pygame.display.update()
