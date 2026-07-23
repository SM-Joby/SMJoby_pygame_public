import pygame,os,time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode([500,500])

path1 = os.path.join("images","rocket.png")
path2 = os.path.join("images","galaxy.png")
image1 = pygame.image.load(path1)
image2 = pygame.image.load(path2)
bg = pygame.transform.scale(image2,(500,500))
rocketx = 250
rockety = 250

keys = [False, False, False, False]#tuple are (), list are []

while rockety<500:
    screen.blit(bg,(0,0))
    screen.blit(image1,(rocketx,rockety))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                keys[0] = True
            elif event.key == pygame.K_2:
                keys[1] = True
            elif event.key == pygame.K_3:
                keys[2] = True
            elif event.key == pygame.K_4:
                keys[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                keys[0] = False
            elif event.key == pygame.K_2:
                keys[1] = False
            elif event.key == pygame.K_3:
                keys[2] = False
            elif event.key == pygame.K_4:
                keys[3] = False
    if keys[0]:
        if rockety>0:
            rockety = rockety-10
    elif keys[1]:
        if rockety<495:
            rockety = rockety+10
    elif keys[2]:
        if rocketx>0:
            rocketx = rocketx-10
    elif keys[3]:
        if rocketx<495:
            rocketx = rocketx+10
    rockety = rockety+10
    time.sleep(2)
print("game over")

