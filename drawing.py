import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(white)


pixAr = pygame.PixelArray(gameDisplay)
pixAr[400][200] = green

pygame.draw.line(gameDisplay,red,(400,300),(400,320),10)
pygame.draw.rect(gameDisplay,green,(500,500,50,30))
pygame.draw.circle(gameDisplay,black,(150,150),85)
pygame.draw.polygon(gameDisplay,blue,((24,99),(500,20),(78,400),(44,80)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
