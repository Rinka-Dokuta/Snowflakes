import pygame
pygame.init()  
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((500, 500))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock


#set up variables for flake 1 position
flake1x = 20
flake1y = -100 #start above the screen

#set up variables for flake 2 position
flake2x = 400
flake2y = -50

#flake 3 position
flake3x = 390
flake3y = -60

#flake 4 position
flake4x = 350
flake4y = -70

#flake 5 position
flake5x = 300
flake5y = -80

#flake 6 position
flake6x = 200
flake6y = -90

#flake 7 position
flake7x = 250
flake7y = -40

#flake 8 position
flake8x = 290
flake8y = -30

#flake 9 position
flake9x = 190
flake9y = -20

#flake 10 position
flake10x = 180 
flake10y = -10

while(1): #omg game lup---------
    clock.tick(60) #FPS
    
    #physics section----
    
    #move flakes
    flake1y+=2 #this one moves faster
    flake2y+=1
    flake3y+=3
    flake4y+=2
    flake5y+=1
    flake6y+=3
    flake7y+=2
    flake8y+=1
    flake9y+=3
    flake10y+=2
    #reset flakes to top of screen
    if flake1y > 500:
        flake1y = -100
    if flake2y > 500:
        flake2y = -50
    if flake3y > 500:
        flake3y = -60
    if flake4y > 500:
        flake4y = -70
    if flake5y > 500:
        flake5y = -80
    if flake6y > 500:
        flake6y = -90
    if flake7y > 500:
        flake7y = -40
    if flake8y > 500:
        flake8y = -30
    if flake9y > 500:
        flake9y = -20
    if flake10y > 500:
        flake10y = -10
    
    
    
    #render section---
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, (255, 255, 255), (flake1x, flake1y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake2x, flake2y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake3x, flake3y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake4x, flake4y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake5x, flake5y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake6x, flake6y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake7x, flake7y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake8x, flake8y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake9x, flake9y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake10x, flake10y), 3)
    pygame.display.flip()#this actually puts the pixel on the screen
   
pygame.quit()
