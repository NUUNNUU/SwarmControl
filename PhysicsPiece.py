# PYGAME PHYSICS PIECE
# NUUNNUU

import time
import math
import random

import pygame

# PHYSICS PARAMETERS
timestep = 10

# PYGAME PARAMETERS
winSize = (1080,720)
colorBack  = (180,180,180)
colorRobot = (255,255,255)
colorLaser = (255,0,0)
colorWall  = (50,50,50)

# BOT DIMENSIONS
botLength = 10 # default
botWidth = 2

class Robot():
    def __init__(self, pos, vec, vel=(0,0), len=botLength, wth=botWidth):
        self.position = pos
        self.vector   = vec
        self.velocity = vel
        self.length   = len
        self.width    = wth
        self.collide  = False
    #
    def updateVel(self, accel=(0,0)):
        self.velocity = (self.velocity[0]+accel[0]*timestep, self.velocity[1]+accel[1]*timestep)
    #
    def updatePos(self):
        self.position = (self.position[0]+self.velocity[0]*timestep, self.position[1]+self.velocity[1]*timestep)
    #
    def updateFric(self): # update velocity in impact of friction
        
        pass
    #
    def posture(self):
        center = self.position
        length = self.length
        angle  = vecAngle(normalize(self.vector))
        head   = (center[0]+(length/2)*math.cos(angle), center[1]+(length/2)*math.sin(angle))
        tail   = (center[0]-(length/2)*math.cos(angle), center[1]-(length/2)*math.sin(angle))
        return center, head, tail
    #
    def model(self):
        head = self.posture()[1]
        tail = self.posture()[2]
        n = math.ceil(self.length/self.width)+1
        circleList = []
        for i in range(n):
            x = (i*head[0] + (n-i)*tail[0])/n
            y = (i*head[1] + (n-i)*tail[1])/n
            circleList.append((x,y))
        return circleList
    #
    def draw(self, win):
        pygame.draw.line(win, colorRobot, self.posture()[1], self.posture()[2], 10)
        pygame.display.update()
#
def normalize(vec):
    mag = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
    return (vec[0]/mag, vec[1]/mag)
#
def vecAngle(vec):
    return math.atan(vec[1]/vec[0])
#
def distance(pos1, pos2):
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)
#
def colBB(bot1, bot2):
    bot1Model = bot1.model()
    bot2Model = bot2.model()
    disMargin = max(bot1.width, bot2.width)
    if bot1.collide != True or bot2.collide != True:
        print("go")
        for i in range(len(bot1Model)):
            for j in range(len(bot2Model)):
                if distance(bot1Model[i], bot2Model[j]) < disMargin:
                    bot1.collide = True
                    bot2.collide = True
                    print("They collide")
                    return
        print("They don't collide")
    else: return#
#
def colLB(laser, bot): # detect collision between laser and bot
    pass
#
Rob = Robot((100,100), (3,0))
Bob = Robot((100, 100), (4,4))

######
if __name__ == "__main__":    
    # initialize environment
    pygame.init()
    pygame.display.set_caption('Simulator')
    win = pygame.display.set_mode(winSize)
    win.fill(colorBack)

    # main loop
    run = True
    while run:
        for bot in bots:
            bot.draw(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #
        keys = pygame.key.get_pressed()
        
        pygame.display.update()
        clock.tick(30) 
        time.sleep(0.03)
