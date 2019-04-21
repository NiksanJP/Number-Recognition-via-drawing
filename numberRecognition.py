from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
import pygame 
import sys
import guesser
import os


#initialize game
pygame.init() 

#Make screen
window_height = 550
window_width = 500

screen = pygame.display.set_mode((window_width, window_height))
canvas = pygame.display.set_mode((window_width, window_height))

#create background
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
yellow = (255,204,0)
orange = (255,100,71)
black = (0,0,0)
pink = (255,200,200)
bgColor_black = (255,255,255)
bgColor_white = (0,0,0)

#Create background
screen.fill(white)

#Make Guess letter
pygame.font.init()
font = pygame.font.SysFont("arial", 40)
def write(guess):
    text = font.render(guess, True, white, black)
    textRect = text.get_rect()
    textRect.center = (250,525)
    screen.blit(text, textRect)
    pygame.display.update()
    

#Make guess bar
pygame.draw.rect(canvas, black, (0,500, 550, 500))

pygame.display.update()

#Guesser
g = guesser.numberGuesser()

while True:
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if left_pressed:
            pygame.draw.circle(canvas, black, (pygame.mouse.get_pos()),5)
            
        if right_pressed:
            canvas.fill(white)
            pygame.draw.rect(canvas, black, (0,500, 550, 500))
            pygame.display.update()
            
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pygame.image.save(screen, "number.png")
                image = Image.open("number.png")
                guess = g.guessNumber()
                write(str(guess))
        
        if event.type == pygame.K_RETURN:
            pygame.image.save(screen, "number.png")
            image = Image.open("number.png")
            guess = g.guessNumber()
            write(str(guess))
    
    pygame.display.update()




