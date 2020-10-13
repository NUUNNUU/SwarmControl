import math
import random
import pygame
import time

# WINDOW 
winSize = (1080,720)

colorBack  = (180,180,180)
colorRobot = (255,255,255)
colorLaser = (255,0,0)
colorWall  = (50,50,50)

# BOT DIMENSIONS
botLength = 10 # default
botWidth = 2

# PHYSICS
radLaser = 5 
fric = 1 
bounce = 1 
bbounce = 1 

####################################################################
class Robot():
    def __init__(self, pos, vec, len=botLength, wth=botWidth):
        self.position = pos
        self.vector   = vec
        self.length   = len
        self.width    = wth 
        self.collide  = False
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
        
class Laser():
    def __init__(self, pos): 
        self.position = pos
    #
    def draw(self, win):
        pygame.draw.circle(win, colorLaser, self.position, radLaser, radLaser-1)
        pygame.display.update()
#
def drawField(win):
    win.fill(colorBack)
    pygame.draw.line(win, colorWall, (10,10), (10,10), 10)
    pygame.draw.line(win, colorWall, (10,510), (510,510), 10)
    pygame.draw.line(win, colorWall, (510,510), (510,10), 10)
    pygame.draw.line(win, colorWall, (510,10), (10,10), 10)
    # map 크기 확장 필요
#
def randomBots(range, n=30,center=(10,10),sigma=1): # randomly set n number of robots in the field 
    # center를 중심으로 sigma 정규분포를 따르는 n개의 로봇 생성    
    pass
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
'''
Start from here
'''
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
def colLB(laser, bot): # detect collision between laser and bot
    pass

if __name__ == "__main__":    
    # initialize environment
    clock = pygame.time.Clock()
    
    pygame.init()
    pygame.display.set_caption('Simulator')
    win = pygame.display.set_mode(winSize)
    win.fill(colorBack) 
    
    # intialize bot 
    bots =[]
    run = True
    while run:
        drawField(win)
        
        for bot in bots:
            bot.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # Terminate game
                if event.key == pygame.K_ESCAPE:  
                    pygame.quit()      
                # Control laser 
                if event.key == pygame.K_LCTRL: 
                    Laser(pygame.mouse.get_pos()).draw(win)
            # Add a robot
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                x,y = pygame.mouse.get_pos()
                bots.append(Robot((x,y),(2,3)))
                
        #physics()
        pygame.display.update()
        clock.tick(30) 
        time.sleep(0.03)
