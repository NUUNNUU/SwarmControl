import numpy as np 

def dist(p1,p2):
    return np.linalg.norm(np.subtract(p1,p2))

def collide_laser_bot(p,c,r):
    flag = False
    p1,p2 = p[0], p[1]    
    v =  np.subtract(p1,p2)
    v_p1 = np.subtract(c,p1)
    v_p2 = np.subtract(c,p2)
    if min(dist(p1,c), dist(p2,c)) <r:
        flag = True         
    if np.linalg.norm(np.dot(v_p1,v))<r
    and np.dot(v_p1, v_p2)<0:
        flag = True 
    return flag 

class Environment():
    def __init__(self, mapSize):
        self.mapsize = mapsize 
        
    def add_obs(self, p1, p2):
        
    def add_bot(self, p_swarm, n_bot):
        
        
        
        
        

if __name__ =="__main__":
    # Parameter setting 
    mapSize =(1920,1200) 
    n_bot = 100 
    n_sampling = 20
    p_init = (10,10)
    p_goal = (50,1000)    
    p_swarm = np.random.randint(30, size=(2,n_bot))
    
    # Create simulation environment 
    envs = Environment(mapSize) # func create_envs including func create_obstacle 
    
