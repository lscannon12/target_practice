import pygame
import random
from pygame import time

pygame.init()
clock = pygame.time.Clock()

#making the screen
(width, height) = (800, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Target Practice")

#BACKGROUND COLOR CHANGES
red_true = True
blue_true = True
green_true = True
red = 0
green = 0
blue = 0

background_colour = (red,green,blue)

def back_changeColor():
    global red, green, blue #tells python "hey, red is ACTUALLY usable here."
    global red_true
    global blue_true
    global green_true
    rand_num = random.randint(0, 100)
    if red_true:
        if red <= 255:
            red += 1
            if red == 255:
                red_true = False
    else:
        red -= 1
        if red == 0:
            red_true = True
    if blue_true:
        if blue <= 250:
            blue += 1
            if blue == 250 or rand_num == 70:
                blue_true = False
    else:
        blue -= 1
        if blue == 0 or rand_num == 70:
            blue_true = True
    if green_true:
        if green <= 250:
            green += 1
            if green == 250 or rand_num == 90:
                green_true = False
    else:
        green -= 1
        if green == 0 or rand_num == 90:
            green_true = True


#CIRCLE COLOR CHANGES
r_true  = True
b_true = True
g_true = True

r = random.randint(0,250)
g = random.randint(0, 250)
b = random.randint(0,250)

def changeColor():
    global r, g, b #tells python "hey, r is ACTUALLY usable here."
    global r_true
    global b_true
    global g_true
    rand_num = random.randint(0, 101) #1 in 50 chance of changing up-shift color to down-shift
    print("Red: ",r)
    print("Blue: ",b)
    if r_true:
        if r <= 255:
            r += 1
            if r == 255 or rand_num == 50:
                r_true = False
    else:
        r -= 1
        if r == 0 or rand_num == 70:
            r_true = True
    if b_true:
        if b <= 250:
            b += 1
            if b == 250 or rand_num == 70:
                b_true = False
    else:
        b -= 1
        if b == 0 or rand_num == 70:
            b_true = True
    if g_true:
        if g <= 250:
            g += 1
            if g == 250 or rand_num == 90:
                g_true = False
    else:
        g -= 1
        if g == 0 or rand_num == 90:
            g_true = True



#running the screen
running = True
while running:
    for event in pygame.event.get():#makes the game QUIT
        if event.type == pygame.QUIT:
            running = False

    back_changeColor() #changes background color
    changeColor() #changes circle colors, or the color of any other object
    pygame.draw.rect(screen, (red,green,blue),(0, 0, width, height)) #rectangle for background

    #ANIMATIONS HERE!! SORRY CPU UR GONNA LAG LIKE  HELL
    pygame.draw.circle(screen, (r,g,b), (400, 250), 200)
    pygame.draw.circle(screen, (red, green, blue), (400, 250), 175)
    pygame.draw.circle(screen, (r, g, b), (400, 250), 150)
    pygame.draw.circle(screen, (red, green, blue), (400, 250), 125)
    pygame.draw.circle(screen, (r, g, b), (400, 250), 100)
    pygame.draw.circle(screen, (red, green, blue), (400, 250), 75)
    pygame.draw.circle(screen, (r, g, b), (400, 250), 50)
    #NO ANIMATIONS PAST HERE
    pygame.display.flip() #function to use ONLY AFTER all screen componants have been configured BEFOREHAND
    clock.tick(40)




