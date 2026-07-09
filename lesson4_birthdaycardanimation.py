import pygame,os
pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("Birthday Card Animation")

#creating a path
#loading images
#scale images to pre set window
path1 = os.path.join("images","happy_birthday.jpg")
image1 = pygame.image.load(path1)
path2 = os.path.join("images","birthday_balloons.jpg")
image2 = pygame.image.load(path2)
path3 = os.path.join("images","birthday_cake.jpg")
image3 = pygame.image.load(path3)

i1 = pygame.transform.scale(image1,(500,500))
i2 = pygame.transform.scale(image2,(500,500))
i3 = pygame.transform.scale(image3,(500,500))

running = True

while running:
    font = pygame.font.SysFont("Calibri Italic",40)
    text = font.render("Hey", True,(102,0,51))
    screen.blit(i1,(0,0))
    screen.blit(text,(50,50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()




