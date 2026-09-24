import pygame, os
pygame.init()
screen = pygame.display.set_mode([700,700])
pygame.display.set_caption("match the following")

path1 = os.path.join("images","archer.png")
game1 = pygame.image.load(path1)
g1 = pygame.transform.scale(game1,(150,150))

path2 = os.path.join("images","ninja.jpg")
game2 = pygame.image.load(path2)
g2 = pygame.transform.scale(game2,(150,150))

path3 = os.path.join("images","wizard.png")
game3 = pygame.image.load(path3)
g3 = pygame.transform.scale(game3,(150,150))

font = pygame.font.SysFont("Calibri Italic",50) #text can't be seen yet!!!
text = font.render("Do you know your fighters and weapons?", True, (255,0,0))

text1 = font.render("Wand", True, (255,255,255))
text2 = font.render("Sword", True, (255,255,255))
text3 = font.render("Bow", True, (255,255,255))

screen.blit(text, (45,45))

screen.blit(text1,(350,150))
screen.blit(text2,(350,275))
screen.blit(text3,(350,400))

screen.blit(g1,(100,150))
screen.blit(g2,(100,275))
screen.blit(g3,(100,475))

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255,0,0), (pos), 20, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(255,0,0),(pos),(pos2),5)
        pygame.draw.circle(screen,(255,0,0),pos2,20,0)
        


    



