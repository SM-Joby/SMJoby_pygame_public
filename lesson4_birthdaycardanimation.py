import pygame,os,time
pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("Birthday Card Animation")

#step1 = creating a path
path1 = os.path.join("images","happy_birthday.jpg")
#step2 = loading selected images
image1 = pygame.image.load(path1)
path2 = os.path.join("images","birthday_balloons.jpg")
image2 = pygame.image.load(path2)
path3 = os.path.join("images","birthday_cake.jpg")
image3 = pygame.image.load(path3)

#step3 = making/scaling the images to fit the premade screen
i1 = pygame.transform.scale(image1,(500,500))
i2 = pygame.transform.scale(image2,(500,500))
i3 = pygame.transform.scale(image3,(500,500))

running = True

while running:
    #choosing a font + size
    font = pygame.font.SysFont("Calibri Italic",40)
    #text
    text = font.render("Hey", True,(102,0,51))
    screen.blit(i1,(0,0))
    screen.blit(text,(50,50))
    pygame.display.update()
    time.sleep(2)
    text2 = font.render("Here are some balloons for you", True, (0,0,0))
    screen.blit(i2,(0,0))
    screen.blit(text2,(50,50))
    pygame.display.update()
    time.sleep(2)
    text3 = font.render("Here is a cake for you", True, (0,0,0))
    screen.blit(i3,(0,0))
    screen.blit(text3,(100,250))
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()




