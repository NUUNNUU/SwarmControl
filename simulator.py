import numpy as np 


class Environment():
    def __init__(self, mapSize, laserSize):
        self.mapSize = mapSize 
        self.laserSize = laserSize 
        self.objects = list() 
        # object의 형식은 [kind, p_center, size, angle]
        # kind = [0:"laser", 1:"robot", 2:"obstacle"]
        # p_center = ["laser","robot": center point, , "obstacle": 꼭지점1]
        # p_size = ["laser","robot": size, , "obstacle": 꼭지점2]
        # angle = ["laser", "obstacle":0 ,"robot": angle[0~pi)]
                
    def add_obs(self, p1, p2):
        # p1,p2는 square block의 꼭지점
        obs = [2,p1,p2,0]
        self.objects.append(obs)
        
    def add_bot(self, p_init, n_bot, ranges=2, size=250 ):
        # initial point 근처에 랜덤하게 로봇 생성
        centers = np.random.randint(p_init,p_init+ranges, size=(2,n_bot))
        angles = np.random.randint(np.pi, size=(n_bot))
        for c,a in (centers, angles):
            self.objects.append([1,c,size,a])
        
    def move_laser(self, p_start, p_end):
        scan_speed = 80 # laser scan speed
        tic = 100       # tic
        disp = np.subtract(p_end,p_start)     # laser displacement
        times = np.norm(disp)*tic//scan_speed
        self.vel = np.multiply(vec,1/times)   # laser displacement per 1 tic
        p_laser = p_start
        for _ in range(times):
            if collide_check_lb(p_laser):                
                push_lb() # laser pushes robots
                if collide_check_bb():
                    push_bb() # robot pushes other robot                   
            p_laser +=vel
                
    def push_lb(self): # laser pushes robots
    def push_bb(self): # robot pushes other robot
    def collide_check_lb(self, p_laser):
    def collide_check_bb(self):
    def collide_check_ob(self):
        

    
    
# def collide_check_lb(): 
#     flag = False
#     p1,p2 = p[0], p[1]    
#     v =  np.subtract(p1,p2)
#     v_p1 = np.subtract(c,p1)
#     v_p2 = np.subtract(c,p2)
#     if min(dist(p1,c), dist(p2,c)) <r:
#         flag = True         
#     if np.linalg.norm(np.dot(v_p1,v))<r
#     and np.dot(v_p1, v_p2)<0:
#         flag = True 
#     return flag 

def dist(p1,p2):
    return np.linalg.norm(np.subtract(p1,p2))
