import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])

game = True

while game:
    screen.fill((255,0,0))#when giving colour you must always give two sets of brackets
    pygame.draw.circle(screen,(155,210,45),(350,230), 40)
    pygame.draw.line(screen,(0,0,0),(150,50),(450, 50),4)
    pygame.draw.rect(screen, (255,255,255), (250,250,10,100))
    pygame.draw.circle(screen,(50,60,70),(100,100),75,5)
    pygame.draw.rect(screen,(110,100,90),(400,300,35,250),5)

                    

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #QUIT is the event to close the pygame window 
            game = False

pygame.quit()


