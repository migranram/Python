import pygame
import math
import random

#Basic variables and pygame init
size = 500
n_phase = 5
win = pygame.display.set_mode(size=(size,size), flags = 0, depth=0, display=0)

#Recursive function
def koch(dist,order, angle, pos):
     if (order > 0):
         #We call recursively the Koch function, dividing the current line into 3 parts
         koch(dist/3.0, order-1,angle,pos)
         koch(dist/3.0, order-1, angle+60,pos)
         koch(dist/3.0, order-1,angle-60,pos)
         koch(dist/3.0, order-1,angle,pos)
         pygame.display.update()
     else:
         #We calculate de final point with a rotation matrix
         posp = [pos[0]+math.cos(angle*2*math.pi/360)*dist,pos[1]-math.sin(angle*2*math.pi/360)*dist] 
         pygame.draw.line(win,(random.randint(70,255),random.randint(70,255),random.randint(70,255)),pos,posp) #We draw a line
         #Update the position
         pos[0]=posp[0]
         pos[1]=posp[1]
         pygame.display.update()

phase = 0
#We draw the different phases of the Fractal
while phase<=n_phase:
    win.fill((0,0,0))
    koch(size,phase,0, [0,size/2])
    #We save the image
    name = 'Koch-Phase_' + str(phase) + '.png'
    pygame.image.save(win, name)
    pygame.display.update()
    #print(phase)
    phase+=1
    