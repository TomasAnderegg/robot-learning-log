import numpy as np 
import matplotlib.pyplot as plt


'''
Build a small grid (4x4 or 5x5) where an agent moves cell by cell with a few special cells (goals,traps). The goal is to create the environment.

'''

class Gridworld:

    def __init__ (self, size=4):

        self.size = size
        self.goal = 10
        self.trap = -10
        self.map = np.full((size,size), -1)
        # self.actions = ['up', 'down', 'left', 'right']
        
        #Setup Goal
        i = np.random.randint(0,size)
        j = np.random.randint(0,size)
        self.map[i,j] = self.goal
        self.goal_pos = (i,j)
    
        #Setup Trap
        #Can be optimized
        i = np.random.randint(0,size)
        j = np.random.randint(0,size)

        while self.map[i,j] == self.goal:

            i = np.random.randint(0,size)
            j = np.random.randint(0,size)

        self.map[i,j] = self.trap
        self.trap_pos = (i,j)

        self.agent_pos = (0,0)
        self.reward = 0
        self.status = 'go'
    
    def gridconst(self):
        # pass
        print(self.agent_pos)
        # print(self.agent_pos[0])
        # print(self.agent_pos[1])
        # print(self.map[self.agent_pos[0],self.agent_pos[1]])
        # print(self.map)
        # print(np.random.randint(self.size))



    def step(self, o_t,a_t):
        # print("valeur", self.agent_pos)
        # print("valeur a_t", a_t)
        if('up'== a_t):
            if o_t[0] != 0:
                o_t = (o_t[0] - 1, o_t[1])
                reward = self.map[o_t[0], o_t[1]]
                if o_t == self.trap_pos:
                    self.status = 'trap'
                elif o_t == self.goal_pos:
                    self.status = 'goal'
                return o_t, reward, self.status
            else:
                reward = -5
                return o_t,  reward, self.status

        if ('down' == a_t): 
            if o_t[0] != (self.size-1):
                o_t = (o_t[0] + 1, o_t[1])
                reward = self.map[o_t[0] , o_t[1]]

                if o_t == self.trap_pos:
                    self.status = 'trap'
                elif o_t == self.goal_pos:
                    self.status = 'goal'
                    
                return o_t,  reward, self.status
            else:
                self.reward = -5
                return o_t,  reward, self.status
    
        if('left' == a_t): 
            if o_t[1] != 0:
                o_t = (o_t[0], o_t[1] - 1)
                reward = self.map[o_t[0], o_t[1]]

                if o_t == self.trap_pos:
                    self.status = 'trap'
                elif o_t == self.goal_pos:
                    self.status = 'goal'

                return o_t,  reward, self.status
            else: 
                reward = -5
                return o_t,  reward, self.status

        if('right' == a_t): 
            if (o_t[1] != (self.size-1)):
                o_t = (o_t[0], o_t[1] + 1)
                reward = self.map[o_t[0], o_t[1]]

                if o_t == self.trap_pos:
                    self.status = 'trap'
                elif o_t == self.goal_pos:
                    self.status = 'goal'

                return o_t,  reward, self.status
            else:
                reward = -5
                return o_t,  reward, self.status
        
        if (self.goal_pos == a_t or self.trap_pos == a_t or 'done'):
            print("completed")
            return o_t,  reward, self.status
    
    def get_map(self):
        return self.map
    
    def reset(self):
        self.agent_pos = (0,self.size-1)
        self.reward = 0
        self.status = 'go'

        return self.agent_pos, self.reward, self.status
        
        
class Agent:
    def __init__(self, reward=0, current_obs = (0,0), map_world = np.full((4,4), -1)):
        self.curr_obs = current_obs
        self.q_values = []
        self.v_values = []
        self.reward = reward
        self.state_val_grid = np.zeros((4,4))
        self.num_actions = 4
        self.map_world = map_world
        self.gamma = 0.2

    def policy(self, step=0):
        'A policy is the way an agent is going to behave in an environment'

        actions_prob = np.random.rand(4, 1)
        max_action_prob = np.argmax(actions_prob) #gives the index of the max value
        # print(actions_prob)
        # print("max value", max_action_prob)

        if max_action_prob == 0:
            return 'up'
        if max_action_prob == 1:
            return 'down'
        if max_action_prob == 2:
            return 'left'
        if max_action_prob == 3:
            return 'right'

    def set_pos_reward(self, o_t, r):
        self.curr_obs = o_t
        self.reward = r 

    def state_function(self):
        'V(s) implementation'

        # state_val_grid = np.array(self.state_val_grid)
        # print(type(state_val_grid))
        for i in range(len(self.state_val_grid)):
            # print(i)
            for j in range(len(self.state_val_grid)):
                # print('j',j)    
                if i ==0 and j == 0:
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i+1][j] + 
                                                                                self.state_val_grid[i][j+1] ))
                elif i == 0 and j != (self.num_actions-1):
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i+1][j] +  
                                                                                self.state_val_grid[i][j+1] +
                                                                                self.state_val_grid[i][j-1] ))
                elif i == 0 and j == (self.num_actions-1):
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i+1][j] +  
                                                                            self.state_val_grid[i][j-1] ))
                elif j == (self.num_actions-1) and i != (self.num_actions-1):
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i+1][j] +  
                                                                                self.state_val_grid[i][j-1] +
                                                                                self.state_val_grid[i-1][j]))
                elif j == (self.num_actions-1) and i == (self.num_actions-1):
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i-1][j] +  
                                                                                self.state_val_grid[i][j-1] ))
                elif j == 0 and i != (self.num_actions-1):
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i+1][j] + 
                                                                                self.state_val_grid[i-1][j] + 
                                                                                self.state_val_grid[i][j+1] )) 
                elif i == (self.num_actions-1) and j == 0:
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i-1][j] + 
                                                                                self.state_val_grid[i][j+1]))
                elif i == (self.num_actions-1) and j != 0:
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i-1][j] + 
                                                                                self.state_val_grid[i][j+1] +
                                                                                self.state_val_grid[i][j-1]))
                else:                
                    self.state_val_grid[i][j] = 1/4*(self.reward + self.gamma*(self.state_val_grid[i+1][j] + 
                                                                                self.state_val_grid[i-1][j] + 
                                                                                self.state_val_grid[i][j+1] +
                                                                                self.state_val_grid[i][j-1] ))
    # state_val_grid = self.state_val_grid.copy() 
        return self.state_val_grid.copy()



if __name__ == "__main__":        

    #World 
    grid = Gridworld(size=4)
    # grid.gridconst()
    # o_t, reward, _= grid.step(o_t=(0,0),a_t='up')
    # print(reward, o_t)

    #Agent
    agent = Agent(reward=0, current_obs=(0,0), map_world=grid.get_map())
    # print(agent.get_pos())
    val_old = np.zeros((4,4))
    val_grid = agent.state_function()
    delta_norm = np.linalg.norm((val_grid - val_old))
    print(val_grid)
    #Rollout
    while delta_norm > 1e-3:
        # print("--------------")
        # a_tp = agent.policy(t)
        # print(a_tp)
        # o_t, reward, _= grid.step(o_t=o_t,a_t=a_tp)
        # print(o_t)
        # agent.set_pos_reward(o_t, reward)
        val_grid = agent.state_function()
        # print("------For sweep: ",t,"-----------------")
        # print(id(val_grid))
        # print(id(val_old))
        delta_norm = np.linalg.norm((val_grid - val_old))
        val_old = val_grid.copy()
        print(delta_norm)

    o_t, reward, status = grid.reset()
    agent.set_pos_reward(o_t, reward)        

