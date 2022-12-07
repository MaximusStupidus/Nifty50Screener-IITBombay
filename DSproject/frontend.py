import pygame
from pygame import mixer
import random
pygame.init() #initialize pygame
length=1000
screen=pygame.display.set_mode((length,750)) #setting screen
pygame.display.set_caption("LUDO KING")
import time
import yash

bg1=pygame.image.load("bg1.jpg")

fonti=pygame.font.Font("freesansbold.ttf",70)
fontii=pygame.font.Font("freesansbold.ttf",22)
fontt=pygame.font.Font("freesansbold.ttf",40)
fonttt=pygame.font.Font("freesansbold.ttf",29)
fontsmol=pygame.font.Font("freesansbold.ttf",20)
font1 = pygame.font.SysFont("comicsansms", 40)
font2 = pygame.font.SysFont("ravie", 40)
font3 = pygame.font.SysFont("gigi", 40)  #not so good
font4 = pygame.font.SysFont("onyx", 40)   #not so good
font5 = pygame.font.SysFont("segoeui", 40)
font6 = pygame.font.SysFont("ebrima", 40)
font7 = pygame.font.SysFont("bodoni", 40)   #good
font8 = pygame.font.SysFont("chiller", 40)
font9 = pygame.font.SysFont("rage", 40)
font10 = pygame.font.SysFont("snapitc", 30) #good
font11= pygame.font.SysFont("comicsansms", 70)
font12= pygame.font.SysFont("comicsansms", 60)
font13= pygame.font.SysFont("comicsansms", 29)

#ALL COUNTERS
overall=0


w1=font11.render("WELCOME! ",True,(255,105,0))
w2=font1.render("TO STOCK MARKET PREDICTOR ",True,(255,105,0))
w3=fontsmol.render("ENTER COMPANY NAME AND THEN PRESS 'tab' TO START ",True,(255,105,0))
w5=fonttt.render("Company name must not be empty ",True,(0,0,0))

color_inactive = (250,200,0)
color_active=(200,0,10)

inputbox1 = pygame.Rect(380, 500, 200, 42)
colour1 = color_inactive
active1=False
PLAYER1NAME = ''

def welc():
    screen.blit(w1,(310,243))
    screen.blit(w2,(200,330))
    screen.blit(w3,(230,400))
    screen.blit(w5,(240,430))
    


def dispinputnames():
    p1=fonttt.render("ENTER THE COMPANY NAME FROM NIFTY50 ",True,(250,205,55))
    


    screen.blit(p1,(200,550))

    #INPUTTING NAME
    colour1 = color_active if active1 else color_inactive
    name1text = fonttt.render(PLAYER1NAME, True, (250,250,250))
    screen.blit(name1text, (inputbox1.x+5, inputbox1.y+5))
    pygame.draw.rect(screen, colour1, inputbox1, 4)



RUNNING=True
lock=1
while RUNNING:
    #print(overall)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            RUNNING=False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the inputbox rectangle.
            if inputbox1.collidepoint(event.pos):
                # Toggle the active variable.
                active1 = not active1
            else:
                active1 = False

    
        if event.type == pygame.KEYDOWN:
            
            if active1:     #if inputing name 1 is active
                if event.key == pygame.K_RETURN:
                    active1=False
                    
                elif event.key == pygame.K_BACKSPACE:
                    PLAYER1NAME = PLAYER1NAME[:-1]
                else:
                    if event.key!=pygame.K_TAB:
                        PLAYER1NAME += event.unicode

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_TAB:
                 if PLAYER1NAME!="" and overall==0:
                    overall=1
                    
                    active1=False

        

                    
                    

                  
                    
    
        
                    


            
                

    #WELCOME SCREEN
    if overall==0:
        screen.fill((50,20,100))
        screen.blit(bg1,(0,0))
        welc()
        dispinputnames()
       
        
        
    if overall==1:
        
        if lock:
            yash.f1(PLAYER1NAME)
            yash.f2()

            yash.f3()
            yash.f4()
            yash.f5()
            yash.f8()
            yash.f9()
            yash.f10()
            yash.f11()
            yash.f12()
            yash.f13()
            yash.f14()
            print("COMPLETE, QUIT PYGAME")
            lock=0


    pygame.display.update()