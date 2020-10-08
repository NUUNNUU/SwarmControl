import numpy as np 
 
def create_envs(mapSize):
    create_obs(envs)

def dist(p1,p2):
    return np.linalg.norm(np.subtract(p1,p2))

def collide_detection_detail(p,c,r):
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

if __name__ =="__main__":
    
    # Create simulation environment 
    envs = create_envs(mapSize) # func create_envs including func create_obstacle 
    
    # Path finding (RRT star) 
    path = create_path(envs, p_init, p_goal)
    
    # object 위치 following도 동시에 진행해야함. 
    while True: 
        mean_swarm, dev_swarm = sampling(p_swarm, n_sampling, n_bot) 
        if dev_swarm > eps_dev:
            move_gather(mean_swarm)
        else:
            closet = search_closet(mean_swarm, path) 
            if dist(path[-1], mean_swarm)< eps_mean:
                break
            move_proceed(closet, mean_swarm)
