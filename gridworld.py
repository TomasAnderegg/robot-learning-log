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

        self.agent_pos = (0,2)
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



    def step(self, a_t):
        # print("valeur", self.agent_pos)
        # print("valeur a_t", a_t)
        if('up'== a_t):
            if self.agent_pos[0] != 0:
                self.agent_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
                self.reward = self.map[self.agent_pos[0], self.agent_pos[1]]
                if self.agent_pos == self.trap_pos:
                    self.status = 'trap'
                elif self.agent_pos == self.goal_pos:
                    self.status = 'goal'
                return self.agent_pos, self.reward, self.status
            else:
                self.reward = -5
                return self.agent_pos, self.reward, self.status

        if ('down' == a_t): 
            if self.agent_pos[0] != (self.size-1):
                self.agent_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
                self.reward = self.map[self.agent_pos[0] , self.agent_pos[1]]

                if self.agent_pos == self.trap_pos:
                    self.status = 'trap'
                elif self.agent_pos == self.goal_pos:
                    self.status = 'goal'
                    
                return self.agent_pos, self.reward, self.status
            else:
                self.reward = -5
                return self.agent_pos, self.reward, self.status
    
        if('left' == a_t): 
            if self.agent_pos[1] != 0:
                self.agent_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
                self.reward = self.map[self.agent_pos[0], self.agent_pos[1]]

                if self.agent_pos == self.trap_pos:
                    self.status = 'trap'
                elif self.agent_pos == self.goal_pos:
                    self.status = 'goal'

                return self.agent_pos, self.reward, self.status
            else: 
                self.reward = -5
                return self.agent_pos, self.reward, self.status

        if('right' == a_t): 
            if (self.agent_pos[1] != (self.size-1)):
                self.agent_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
                self.reward = self.map[self.agent_pos[0], self.agent_pos[1]]

                if self.agent_pos == self.trap_pos:
                    self.status = 'trap'
                elif self.agent_pos == self.goal_pos:
                    self.status = 'goal'

                return self.agent_pos, self.reward, self.status
            else:
                self.reward = -5
                return self.agent_pos, self.reward, self.status
        
        if (self.goal_pos == a_t or self.trap_pos == a_t or 'done'):
            print("completed")
            return self.agent_pos, self.reward, self.status
    def reset(self):
        self.agent_pos = (0,self.size-1)
        self.reward = 0
        self.status = 'go'

        return self.agent_pos, self.reward, self.status
        

        
class Agent:
    def __init__(self, reward=0, current_obs = (0,0)):
        self.curr_obs = current_obs
        self.q_values = []
        self.v_values = []
        self.reward = reward

    def action(self, step=0):
        # print(step)
        if step == 0:
            step +=1
            return 'up'
        elif step == 1:
            step +=1
            return 'right'
        elif step == 2:
            step +=1 
            return 'down'
        elif step == 3:
            step +=1
            return 'left'
        elif step == 4:
            return 'done'
    def set_pos_reward(self, o_t, r):
        self.curr_obs = o_t
        self.reward = r + self.reward

    # def get_pos(self):
    #     print(self.curr_obs)

if __name__ == "__main__":        

    #World 
    grid = Gridworld(size=4)
    # grid.gridconst()
    o_t, reward, _= grid.step(a_t='up')
    # print(reward, o_t)

    #Agent
    agent = Agent(reward=0, current_obs=o_t)
    # print(agent.get_pos())

    #Rollout
    for t in range(5):
        print("--------------")
        a_tp = agent.action(t)
        print(a_tp)
        o_t, reward, _= grid.step(a_t=a_tp)
        # print(o_t)
        agent.set_pos_reward(o_t, reward)

    o_t, reward, status = grid.reset()
    agent.set_pos_reward(o_t, reward)        

