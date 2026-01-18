# pyGame.py
# A simple pygame script that initializes a window and prints types of objects.

import pygame
import random
import sys

pygame.init()

# Constants for the original game's screen/grid size
# ZX Spectrum screen is 32 columns x 24 rows (approx)

# Colour Definitions
rgbBLACK = (0, 0, 0)
rgbRED = (200, 0, 0)
rgbGREEN = (0, 200, 0)
rgbBLUE = (0, 0, 200)
rgbYELLOW = (200, 200, 0)
rgbCYAN = (0, 200, 200)
rgbMAGENTA = (200, 0, 200)
rgbWHITE = (255, 255, 255)

# Screen dimensions

scrAREA = scrWIDTH, scrHEIGHT = 640, 480
scrSIZE = 20

print(type(scrAREA))

gameDisplay = pygame.display
gameScreen = gameDisplay.set_mode( scrAREA )

gameDisplay.set_caption( "Thru' The Wall" )

print( type( gameScreen ) )

# Outer loop
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    # Inner loop


    gameScreen.fill( rgbBLACK )
    pygame.display.update()
    

print( "Exiting..." )
pygame.quit()
sys.exit()


