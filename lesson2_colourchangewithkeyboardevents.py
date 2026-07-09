import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])

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
        

    def draw(self,surface):
        pygame.draw.rect(surface,self.colour,(self.x,self.y,self.length,self.width))

x = 250
y = 250
l = 80
w = 20

r1 = rectangle(green,x,y,l,w)
r2 = rectangle(magenta,x,y,l,w)
r3 = rectangle(yellow,x,y,l,w)
screen.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type ==pygame.KEYDOWN:#checking key
            if event.key==pygame.K_g:
                screen.fill((255,255,255))
                r1.draw(screen)
                pygame.display.update()
            elif event.key == pygame.K_m:
                screen.fill((255,255,255))
                r2.draw(screen)
                pygame.display.update()
            elif event.key == pygame.K_y:
                screen.fill((255,255,255))
                r3.draw(screen)
                pygame.display.update()
    pygame.display.update()


    #keydown calling the event and K_...connects the keydown event to the actual key
    #fix indentation in while loop