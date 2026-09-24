import pygame, os
pygame.init()
screen = pygame.display.set_mode([700,700])
pygame.display.set_caption("match the following")

path1 = os.path.join("images","candy_crush.jpg")
game1 = pygame.image.load(path1)

path2 = os.path.join("images","ludo.png")
game2 = pygame.image.load(path2)

path3 = os.path.join("images","subsurfs.png")
game3 = pygame.image.load(path3)

path4 = os.path.join("images","templerun.png")
game4 = pygame.image.load(path4)

font = pygame.font.SysFont("Calibri Italic",50) #text can't be seen yet!!!
text = font.render("Do you know your games?", True, (255,0,0))

text1 = font.render("Subway Surfers", True, (255,255,255))
text2 = font.render("temple Run", True, (255,255,255))
text3 = font.render("candy Crush", True, (255,255,255))
text4 = font.render("Ludo", True, (255,255,255))

screen.blit(text, (45,45))

screen.blit(text1,(350,100))
screen.blit(text2,(350,225))
screen.blit(text3,(350,350))
screen.blit(text4,(350,475))

screen.blit(game1,(100,100))
screen.blit(game2,(100,225))
screen.blit(game3,(100,350))
screen.blit(game4,(100,475))
pygame.display.update()

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255,0,0), (pos), 20, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(255,0,0),(pos),(pos2),5)
        pygame.draw.circle(screen,(255,0,0),(pos2),20,0)
        pygame.display.update()
        


    



