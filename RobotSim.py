import pygame

import math
import random
import pygame
import time

# Global parameters 
winSize = (1080,720)
colorBack  = (180,180,180)
colorRobot = (255,255,255)
colorLaser = (255,0,0)
colorWall  = (50,50,50)

radLaser = 5 
fric = 1 
bounce = 1 
bbounce = 1 

####################################################################
class Robot():
    def __init__(self, pos, vec, leng):
        self.position = pos
        self.vector = vec
        self.leng = leng 
    
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
        
class Laser():
    def __init__(self, pos): 
        self.position = pos
    
    def draw(self, win):
        pygame.draw.circle(win, colorLaser, self.position, radLaser, radLaser-1)
        pygame.display.update()
        
        
def drawField(win):
    win.fill(colorBack)
    pygame.draw.line(win, colorWall, (10,10), (10,10), 10)
    pygame.draw.line(win, colorWall, (10,510), (510,510), 10)
    pygame.draw.line(win, colorWall, (510,510), (510,10), 10)
    pygame.draw.line(win, colorWall, (510,10), (10,10), 10)
    # obstacle wall 추가 필요
    # map 크기 확장 필요
    
def randomBots(range, n=30,center=(10,10),sigma=1): # randomly set n number of robots in the field 
    # center를 중심으로 sigma 정규분포를 따르는 n개의 로봇 생성    
    pass

def normalize(vec):
    mag = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
    return (vec[0]/mag, vec[1]/mag)

def physics():
    pass 

if __name__ == "__main__":    
    # initialize environment
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Sim')
    win = pygame.display.set_mode(winSize)
    win.fill(colorBack) 
    
    # intialize bot 
    bots =[]    
    # bots = randomBots()
            
    ###############
    ## main loop ##
    ###############
    while True:      
        drawField(win) 
        for bot in bots:
            bot.draw(win)  
        for event in pygame.event.get():
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
                bots.append(Robot((x,y),(2,3),0))
                
        #physics() # 물리엔진 구현필요     
        pygame.display.flip() # update와 같은 기능 
        clock.tick(30) 
        time.sleep(0.03)
