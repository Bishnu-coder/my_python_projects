from hashlib import shake_128
import pygame
from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_p
import random
from pygame import mixer

pygame.init()
pygame.mixer.init()

start=pygame.mixer.music.load("start.m4a")
white=(255,255,255)
w1=pygame.image.load('welcome.png')
background ='Background.jpg'
player ='player.jpg'
width = 1000
height= 700
GAME_SPRITES={}
GAME_SPRITES['Background'] = pygame.image.load(background)
GAME_SPRITES['player'] = pygame.image.load(player)
h2= pygame.transform.rotate(pygame.image.load('h2.jpg'),180)
h3= pygame.transform.rotate(pygame.image.load('h3.jpg'),180)
game=False
game_over=False


s1=7.5


fps=120
fps_clock=pygame.time.Clock()
velx=300
vely=500
screeny=0
screeny2=-350

h2x=random.randrange(0,500)
h3x=random.randrange(500,1000)
h2y=0
h3y=0

over= 'image/over.jpg'
over1= pygame.image.load(over)

score=0

pause=False
p1=pygame.image.load('image/pause.jpg')

r1=random.randint(600,750)
r2=random.randint(600,750)


screen = pygame. display. set_mode((width, height))
pygame. display. set_caption('save the car')

mixer.music.set_volume(0.7)




while True :
    for event in pygame.event.get() :
            
                    if event.type == pygame.QUIT :
                        game=False                   
                        pygame.quit()
                    
                    if event.type == pygame.KEYDOWN and (event.key ==K_LEFT):
                            game=True
                            game_over=False
                            velx-=150
                    if event.type == pygame.KEYDOWN and (event.key ==K_RIGHT):
                            game=True
                            game_over=False
                            velx+=150
                    if event.type == pygame.KEYDOWN and (event.key==K_DOWN):
                            game==False                       
                            pause=True
                            

                    if event.type == pygame.KEYDOWN and (event.key==K_SPACE):
                            game==True
                            pause=False
                            game_over=False

    screen.blit(GAME_SPRITES['Background'],(0,screeny))      
    screen.blit(GAME_SPRITES['player'],(velx,vely))
    screen.blit(h2,(h2x,h2y))
    screen.blit(h3,(h3x,h3y))

    

    if game==True and pause == False:
            screeny+=s1
            vely-=5
            h2y+=5
            h3y+=5
                 
            
    
    if vely==390:
        vely=395
    if screeny==300:
        screeny=0
    if(h2y >= 700 and game==True and game_over==False and pause==False):
        score+=0
        h2y=h2y-r1
        h2x = random.randint(0,500)
         
    
            
    if(h3y >= 700 and game==True and game_over==False and pause==False):
        score+=5 
        h3y=h3y-r2
        h3x = random.randint(500,900)
    print()

    if abs(velx - h2x)<90 and abs(vely - h2y)<90 and pause==False:
        score=0
        game_over=True
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound\crash.m4a'))  
        
    if abs(velx - h3x)<90 and abs(vely - h3y)<90 and pause==False:
        score=0
        game_over=True
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound\crash.m4a'))
    if game_over==True :
        screen.blit(over1,(0,0))
             
    if game==False:
        screen.blit(w1,(0,0))
    if pause==True:
        screen.blit(p1,(0,0))
    

    


    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)

    
    text = font.render(str(score), True, green, blue)
    
    screen.blit(text, (900,10))

    pygame.display.update()
    fps_clock.tick(fps)
