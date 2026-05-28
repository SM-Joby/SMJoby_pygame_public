import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])

game = True

while game:
    screen.fill((0,255,0))
    pygame.draw.circle(screen,(0,100,100),(150,430), 40)
    pygame.draw.line(screen,(150,0,100),(350,300),(450, 50),4)
    pygame.draw.rect(screen, (10,95,65), (210,50,10,100))
    pygame.draw.circle(screen,(15,155,255),(57,84),75,5)
    pygame.draw.rect(screen,(20,200,95),(236,378,35,250),5)

    pygame.display.update()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            game = False

pygame.quit()