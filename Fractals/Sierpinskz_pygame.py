import math
import pygame

#Basic Variables
boxSize = 300
size = 3*boxSize
phase = 0
n_phase = 5

#Pygame initialization
win = pygame.display.set_mode(size=(size,size), flags = 0, depth=0, display=0)

#Main loop through all the phases
while phase < n_phase:
    i = math.pow(3,phase) -1
    while i >= 0:
            #We calculate the X and Y position of the boxes
            posx = -(boxSize/2) + size/(math.pow(3,phase)*2) + size/(math.pow(3,phase))*i
            j = math.pow(3,phase) -1
            while j >= 0:    
                posy = -(boxSize/2) + size/(math.pow(3,phase)*2) + size/(math.pow(3,phase))*j
                pygame.draw.rect(win,(255,255,255),pygame.Rect(posx,posy,boxSize,boxSize))
                j-=1
                pygame.display.update() #Update the display to show changes
            i-=1    
    
    #We save the image
    name = 'Phase_' + str(phase) + '.png'
    pygame.image.save(win, name)
    #Update the variables
    boxSize/=3
    phase+=1