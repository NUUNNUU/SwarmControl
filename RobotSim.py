import math
import random
import pygame
import time

winSize = (1080,720)

colorBack  = (100,100,100)
colorRobot = (255,255,255)
colorLaser = (255,0,0)
colorWall  = (50,50,50)

####################################################################
class Robot():
    def __init__(self, pos, vec, len):
        self.position = pos
        self.vector = vec
        self.length = len
    #
    def posture(self):
        center = self.position
        vector = unitVec(self.vector)
        head   = (center[0]+vector[0]/2, center[1]+vector[1]/2)
        tail   = (center[0]-vector[0]/2, center[1]-vector[1]/2)
        return center, head, tail
    #
    def draw(self, win):
        #pygame.draw.circle(win, colorRobot, self.position, 2,2)
        pygame.draw.line(win, colorRobot, self.posture()[1], self.posture()[2], 10)
        pygame.display.update()
    #
#
def drawField(win):
    win.fill(colorBack)
    pygame.draw.line(win, colorWall, (10,10), (10,510), 10)
    pygame.draw.line(win, colorWall, (10,510), (510,510), 10)
    pygame.draw.line(win, colorWall, (510,510), (510,10), 10)
    pygame.draw.line(win, colorWall, (510,10), (10,10), 10)
#
def randomBots(range, n): # randomly set n number of robots in the field
    #for i in range(n):
    pass
#
def unitVec(vec):
    mag = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
    return (vec[0]/mag, vec[1]/mag)


#Rob = Robot((1,1), (3,1), 3)

####################################################################

if __name__ == "__main__":
    botList = []
    clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption('Sim')
    win = pygame.display.set_mode(winSize)
    win.fill(colorBack)
    
    run = True
    while run:
        pygame.time.delay(30)
        drawField(win)

        for bot in botList:
            bot.draw(win)
        
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # terminate
                run = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN: # add a robot
                x,y = pygame.mouse.get_pos()
                botList= [Robot((x,y), (2,3),0)]
                #botList.append(Robot((x,y), 0,0))
                
        #pygame.display.update()

