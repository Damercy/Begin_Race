import pygame 
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

dim_red = (200,0,0)
dim_white = (200,200,200)

car_width = 111

gameDisplay = pygame.display.set_mode((display_width ,display_height))
pygame.display.set_caption('The GAME!')
clock = pygame.time.Clock()

carImg = pygame.image.load('car_mod.png')


def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count)+" objects!",True,white)
    gameDisplay.blit(text,(0,0))

    
def things (thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    if text == 'START' or text == 'EXIT':
        textSurface = font.render(text ,True,black)
        return textSurface,textSurface.get_rect()

    textSurface = font.render(text ,True,white)
    return textSurface,textSurface.get_rect()

def game_exit():
    pygame.quit()
    quit()

    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',120)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit (TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('Crashed!')

def button(msg,x,y,w,h,color_active,color_inactive,action=None):
    
        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()
        
        pygame.draw.rect(gameDisplay,color_inactive,(x,y,w,h))
        pygame.draw.rect(gameDisplay,color_inactive,(x,y,w,h))

        if (x+w>mouse[0]>x) and (y+h>mouse[1]>y):
            pygame.draw.rect(gameDisplay,color_active,(x,y,w,h))
            if click[0] == 1 and action!=None:
                action()
        
        smallText = pygame.font.Font("freesansbold.ttf",10)
        TextSurf, TextRect = text_objects(msg,smallText)
        TextRect.center = (((2*x+w)/2,(2*y+h)/2))
        gameDisplay.blit(TextSurf,TextRect)


def intro_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects('Welcome to THE GAME!',largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit (TextSurf,TextRect)

        button('START',150,450,100,50,dim_white,white,game_loop)
        button('EXIT',550,450,100,50,dim_white,white,game_exit)
            
        pygame.display.update()
        clock.tick(60)

    
def game_loop():
    x= (display_width * 0.5)
    y = (display_height * 0.5)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0,display_width-100)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    dodged = 0
    inc_speed = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                    x_change = 0
                    y_change = 0


        x+= x_change
        y+= y_change

        gameDisplay.fill(black)
    
        things(thing_startx,thing_starty,thing_width,thing_height,blue)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
  
        if x > display_width - car_width or x< 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            dodged+= 1
            inc_speed+=1
            if inc_speed  > 10:
                thing_speed+= 1
                inc_speed = 0
            thing_startx = random.randrange(0,display_width-100)

        if y < thing_starty + thing_height:
            if (x > thing_startx and x < thing_startx + thing_width) or (x+car_width > thing_startx and x+car_width < thing_startx + thing_width):
                crash()
            
        pygame.display.update()
        clock.tick(60)

intro_screen()

