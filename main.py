#imports
import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_d, K_p
import random
from pygame import mixer
# for sound
pygame.init()
pygame.mixer.init()
#loading data and some game logic
white=(255,255,255)
w1=pygame.image.load('welcome.png')
width = 1000
height= 700
background = pygame.image.load('background.jpg')
player = pygame.image.load('player.jpg')
h2= pygame.transform.rotate(pygame.image.load('h2.jpg'),180)
h3= pygame.transform.rotate(pygame.image.load('h3.jpg'),180)
game=False
game_over=False
s1=150
#fps and screen related
fps=60
whole_run=True
fps_clock=pygame.time.Clock()
velx=300
vely=700
screeny=0
screeny2=-350
#hurddle car related
h2x=random.randrange(0,500)
h3x=random.randrange(500,1000)
h2y=-10
h3y=-10
over= 'over.jpg'
over1= pygame.image.load(over)
score=0
dbg=False
pause=False
car_move=True
p1=pygame.image.load('pause.jpg')
r1=random.randint(600,750)
r2=random.randint(600,750)
font = pygame.font.Font('freesansbold.ttf', 32)
key_left=False
key_right=False
#for playing back ground sound
pygame.mixer.Channel(1).play(pygame.mixer.Sound('start.m4a'))
screen = pygame. display. set_mode((width, height))
pygame. display. set_caption('save the car')
mixer.music.set_volume(0.5)
f= open("highscore.txt","r")
highscore=f.read()
while whole_run:
    for event in pygame.event.get() :
                    if event.type == pygame.QUIT:       
                        whole_run=False
                    if whole_run==True:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('start.m4a'))
                    if event.type == pygame.KEYDOWN and (event.key ==K_LEFT) :
                            game=True
                            game_over=False
                            key_left=True
                    if event.type == pygame.KEYUP and (event.key ==K_LEFT):
                        key_left=False
                    if event.type == pygame.KEYDOWN and (event.key ==K_RIGHT) :
                            game=True
                            game_over=False
                            key_right=True
                    if event.type == pygame.KEYUP and (event.key ==K_RIGHT):
                        key_right=False
                    if event.type == pygame.KEYDOWN and (event.key==K_p):
                            game==False                       
                            pause=True
                    if event.type == pygame.KEYDOWN and (event.key==K_SPACE):
                            game==True
                            pause=False
                            game_over=False
                    if event.type == pygame.KEYDOWN and (event.key==K_d):
                            dbg=True
                    
                    if event.type == pygame.KEYDOWN and (event.key==K_UP) and dbg==True:
                        fps+=1
                    if event.type == pygame.KEYDOWN and (event.key==K_DOWN) and dbg==True:
                        fps-=1
    screen.blit(background,(0,screeny))      
    screen.blit(player,(velx,vely))
    screen.blit(h2,(h2x,h2y))
    screen.blit(h3,(h3x,h3y))
    if game==True and key_right==True:
        velx+=10
    if game==True and key_left==True:
        velx-=10
    if game==True and pause == False:
            screeny+=s1
            vely-=5
            h2y+=5
            h3y+=5
    if score>int(highscore):
        highscore=score
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
    if abs(velx - h2x)<90 and abs(vely - h2y)<90 and pause==False:
        score=0
        game_over=True
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('crash.m4a'))  
    if abs(velx - h3x)<90 and abs(vely - h3y)<90 and pause==False:
        score=0
        game_over=True
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('crash.m4a'))
    if game_over==True :
        screen.blit(over1,(0,0))
        with open("highscore.txt","w")as f:
            f.write(str(highscore))
    if game==False :
        screen.blit(w1,(0,0))
    if pause==True :
        screen.blit(p1,(0,0))
    if dbg==True:
        text = font.render("fps="+str(fps), True, green, blue)
        screen.blit(text, (850,50))
    if game==True and velx>=900:
        velx-=20
    if game==True and velx<=0:
        velx+=20
    green = (0, 255, 0)
    blue = (0, 0, 128)
    text = font.render("score="+str(score), True, green, blue)
    screen.blit(text, (850,10))
    text = font.render("Highscore="+str(highscore), True, green, blue)
    screen.blit(text, (0,10))
    pygame.display.update()
    fps_clock.tick(fps)
#end of game