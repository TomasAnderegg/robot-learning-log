import numpy as np 
import matplotlib.pyplot as plt


'''
Build a small grid (4x4 or 5x5) where an agent moves cell by cell with a few special cells (goals,traps). The goal is to create the environment.

'''

ROLLOUT = 1

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
        print(self.map)
        # print(np.random.randint(self.size))



    def step(self, o_t,a_t):
        # print("valeur", self.agent_pos)
        # print("valeur a_t", a_t)
        if('still' == a_t):
            self.status = 'still'
            return o_t, a_t, self.status
        if('up'== a_t):
            if o_t[0] != 0:
                o_t = (o_t[0] - 1, o_t[1])
                self.reward = self.map[o_t[0], o_t[1]]
                if o_t == self.trap_pos:
                    self.status = 'trap'
                elif o_t == self.goal_pos:
                    self.status = 'goal'
                return o_t, self.reward, self.status
            else:
                self.reward = -5
                return o_t,  self.reward, self.status

        if ('down' == a_t): 
            if o_t[0] != (self.size-1):
                o_t = (o_t[0] + 1, o_t[1])
                self.reward = self.map[o_t[0] , o_t[1]]

                if o_t == self.trap_pos:
                    self.status = 'trap'
                elif o_t == self.goal_pos:
                    self.status = 'goal'
                    
                return o_t,  self.reward, self.status
            else:
                self.reward = -5
                return o_t,  self.reward, self.status
    
        if('left' == a_t): 
            if o_t[1] != 0:
                o_t = (o_t[0], o_t[1] - 1)
                self.reward = self.map[o_t[0], o_t[1]]

                if o_t == self.trap_pos:
                    self.status = 'trap'
                elif o_t == self.goal_pos:
                    self.status = 'goal'

                return o_t,  self.reward, self.status
            else: 
                self.reward = -5
                return o_t,  self.reward, self.status

        if('right' == a_t): 
            if (o_t[1] != (self.size-1)):
                o_t = (o_t[0], o_t[1] + 1)
                self.reward = self.map[o_t[0], o_t[1]]

                if o_t == self.trap_pos:
                    self.status = 'trap'
                elif o_t == self.goal_pos:
                    self.status = 'goal'

                return o_t,  self.reward, self.status
            else:
                self.reward = -5
                return o_t,  self.reward, self.status
        
        if (self.goal_pos == a_t or self.trap_pos == a_t or 'done'):
            print("completed")
            return o_t,  self.reward, self.status
    
    def get_map(self):
        return self.map
    def reset(self):
        pass
    
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

    def policy(self, value=(1/4,1/4,1/4,1/4)): #up, down, left, right
        'A policy is the way an agent is going to behave in an environment'

        actions_prob = value
        # max_action_prob = np.argmax(actions_prob) #gives the index of the max value
        # print(actions_prob)
        # print("max value", max_action_prob)
        
        
        return actions_prob
    

    def set_pos_reward(self, o_t, r):
        self.curr_obs = o_t
        self.reward = r 

    # def policy_eval(self,policy):
    #     'V(s) implementation'

    #     # state_val_grid = np.array(self.state_val_grid)
    #     # print(type(state_val_grid))
    #     for i in range(len(self.state_val_grid)):
    #         # print(i)
    #         for j in range(len(self.state_val_grid)):
    #             # print('j',j)    
    #             for k in range(len(policy)):
    #                 if i ==0 and j == 0:
    #                     self.state_val_grid[i][j] = policy[k]*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i+1][j] + 
    #                                                                                 self.state_val_grid[i][j+1] ))
    #                 elif i == 0 and j != (self.num_actions-1):
    #                     self.state_val_grid[i][j] = 1/4*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i+1][j] +  
    #                                                                                 self.state_val_grid[i][j+1] +
    #                                                                                 self.state_val_grid[i][j-1] ))
    #                 elif i == 0 and j == (self.num_actions-1):
    #                     self.state_val_grid[i][j] = 1/4*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i+1][j] +  
    #                                                                             self.state_val_grid[i][j-1] ))
    #                 elif j == (self.num_actions-1) and i != (self.num_actions-1):
    #                     self.state_val_grid[i][j] = 1/4*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i+1][j] +  
    #                                                                                 self.state_val_grid[i][j-1] +
    #                                                                                 self.state_val_grid[i-1][j]))
    #                 elif j == (self.num_actions-1) and i == (self.num_actions-1):
    #                     self.state_val_grid[i][j] = 1/4*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i-1][j] +  
    #                                                                                 self.state_val_grid[i][j-1] ))
    #                 elif j == 0 and i != (self.num_actions-1):
    #                     self.state_val_grid[i][j] = 1/4*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i+1][j] + 
    #                                                                                 self.state_val_grid[i-1][j] + 
    #                                                                                 self.state_val_grid[i][j+1] )) 
    #                 elif i == (self.num_actions-1) and j == 0:
    #                     self.state_val_grid[i][j] = 1/4*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i-1][j] + 
    #                                                                                 self.state_val_grid[i][j+1]))
    #                 elif i == (self.num_actions-1) and j != 0:
    #                     self.state_val_grid[i][j] = 1/4*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i-1][j] + 
    #                                                                                 self.state_val_grid[i][j+1] +
    #                                                                                 self.state_val_grid[i][j-1]))
    #                 else:                
    #                     self.state_val_grid[i][j] = 1/4*(self.map_world[i][j] + self.gamma*(self.state_val_grid[i+1][j] + 
    #                                                                                 self.state_val_grid[i-1][j] + 
    #                                                                                 self.state_val_grid[i][j+1] +
    #                                                                                 self.state_val_grid[i][j-1] ))
    # # state_val_grid = self.state_val_grid.copy() 
    #     return self.state_val_grid
    def policy_eval(self,step, policy):
            'V(s) implementation'
    
            # state_val_grid = np.array(self.state_val_grid)
            # print(type(state_val_grid))
            for i in range(len(self.state_val_grid)):
                # print(i)
                for j in range(len(self.state_val_grid)):
                    # print('j',j)
                    o_t_up,reward_up,_ = step((i,j),'up')
                    o_t_down,reward_down,_ = step((i,j),'down')
                    o_t_left,reward_left,_ = step((i,j),'left')
                    o_t_right,reward_right,_ = step((i,j),'right')

                    self.state_val_grid[i][j] = (policy[0]*(reward_up + self.gamma*(self.state_val_grid[o_t_up[0]][o_t_up[1]])) +
                                                policy[1]*(reward_down + self.gamma*(self.state_val_grid[o_t_down[0]][o_t_down[1]])) + 
                                                policy[2]*(reward_left + self.gamma*(self.state_val_grid[o_t_left[0]][o_t_left[1]])) +
                                                policy[3]*(reward_right + self.gamma*(self.state_val_grid[o_t_right[0]][o_t_right[1]]))                                           
                                                ) 
                                                       
        # state_val_grid = self.state_val_grid.copy() 
            return self.state_val_grid
    

    def policy_improvement(self):
        'V(s) implementation'
        # print("valeur dans policy improvement:", self.state_val_grid)
        val_grid_opt = np.zeros((4,4))
        action_grid = np.zeros((4,4))
        trap = np.min(self.state_val_grid)
        goal = np.max(self.state_val_grid)
        print("trap value", trap)
        print("goal value", goal)
        # print(type(state_val_grid))
        for i in range(len(val_grid_opt)):
            # print(i)
            for j in range(len(val_grid_opt)):
                # print('j',j)
                if not(goal != self.state_val_grid[i][j]) or (trap != self.state_val_grid[i][j]):    
                    if i ==0 and j == 0:
                        # val_grid_opt[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i+1][j], 
                        #                                                             self.state_val_grid[i][j+1] )))

                        action_grid[i][j] = np.argmax((0,self.state_val_grid[i+1][j],self.state_val_grid[i][j+1],0,0))
                    elif i == 0 and j != (self.num_actions-1):
                        # self.state_val_grid[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i+1][j],  
                        #                                                             self.state_val_grid[i][j+1],
                        #                                                             self.state_val_grid[i][j-1] )))

                        action_grid[i][j] = np.argmax((0,self.state_val_grid[i+1][j],self.state_val_grid[i][j-1],self.state_val_grid[i][j+1],0 ))
                    elif i == 0 and j == (self.num_actions-1):
                        # self.state_val_grid[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i+1][j],  
                        #                                                         self.state_val_grid[i][j-1] )))

                        action_grid[i][j] = np.argmax((0,self.state_val_grid[i+1][j],self.state_val_grid[i][j-1],0,0 ))

                    elif j == (self.num_actions-1) and i != (self.num_actions-1):
                        # self.state_val_grid[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i+1][j],  
                        #                                                             self.state_val_grid[i][j-1],
                        #                                                             self.state_val_grid[i-1][j])))

                        action_grid[i][j] = np.argmax((self.state_val_grid[i-1][j], self.state_val_grid[i+1][j],self.state_val_grid[i][j-1],0,0))

                    elif j == (self.num_actions-1) and i == (self.num_actions-1):
                        # self.state_val_grid[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i-1][j],  
                        #                                                             self.state_val_grid[i][j-1] )))

                        action_grid[i][j] = np.argmax((self.state_val_grid[i-1][j],0,self.state_val_grid[i][j-1],0,0 ))

                    elif j == 0 and i != (self.num_actions-1):
                        # self.state_val_grid[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i+1][j], 
                        #                                                             self.state_val_grid[i-1][j], 
                        #                                                             self.state_val_grid[i][j+1] ))) 

                        action_grid[i][j] = np.argmax((0, self.state_val_grid[i+1][j], self.state_val_grid[i-1][j], self.state_val_grid[i][j+1],0 ))

                    elif i == (self.num_actions-1) and j == 0:
                        # self.state_val_grid[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i-1][j], 
                        #                                                             self.state_val_grid[i][j+1])))

                        action_grid[i][j] = np.argmax((self.state_val_grid[i-1][j],0,0, self.state_val_grid[i][j+1],0))

                    elif i == (self.num_actions-1) and j != 0:
                        # self.state_val_grid[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i-1][j], 
                        #                                                             self.state_val_grid[i][j+1],
                        #                                                             self.state_val_grid[i][j-1])))

                        action_grid[i][j] = np.argmax((self.state_val_grid[i-1][j],0, self.state_val_grid[i][j-1],self.state_val_grid[i][j+1],0))
                    else:                
                        # self.state_val_grid[i][j] = (self.map_world[i][j] + self.gamma*np.max((self.state_val_grid[i+1][j], 
                        #                                                             self.state_val_grid[i-1][j], 
                        #                                                             self.state_val_grid[i][j+1],
                        #                                                             self.state_val_grid[i][j-1] )))

                        action_grid[i][j] = np.argmax((self.state_val_grid[i-1][j], self.state_val_grid[i+1][j], self.state_val_grid[i][j-1],self.state_val_grid[i][j+1],0 ))
                else:
                    action_grid[i][j] = np.argmax((0,0,0,0,1))
    # state_val_grid = self.state_val_grid.copy() 
        return self.state_val_grid, action_grid
    
    def set_val_grid(self, val_grid = np.zeros((4,4))):
        self.state_val_grid = val_grid

    def optimal_policy(self, val_grid = np.zeros((4,4))):
        pass



if __name__ == "__main__":        

    #World 
    grid = Gridworld(size=4)
    grid.gridconst()
    # grid.reset()
    # o_t, reward, _= grid.step(o_t=(3,0),a_t='down')
    # print("grid:",reward, o_t)

    #Agent
    agent = Agent(reward=0, current_obs=(0,0), map_world=grid.get_map())
    # print(agent.get_pos())
    
    # print("policy:", agent.policy().shape)
    val_old = np.zeros((4,4))
    for i in range(ROLLOUT):
        delta_norm = np.linalg.norm(val_old - agent.policy_eval(grid.step,agent.policy(value= (1/4,1/4,1/4,1/4))))
        print("delta:-------", delta_norm)
        while delta_norm > 1e-3:

            val_grid = agent.policy_eval(grid.step,agent.policy(value= (1/4,1/4,1/4,1/4)))

            #Policy Evaluation
            delta_norm = np.linalg.norm((val_grid - val_old))
            val_old = val_grid.copy()
            print("delta norm", delta_norm)

        print("V_pi finale", val_grid)

        agent.set_val_grid(val_grid=val_grid)

        'Up to now, we have the V_pi converged. Now, we need to improve the policy'

        #Optimal Value Function: Policy Improvement

        # val_old_opt = np.zeros((4,4))
        val_opt_current,action_grid = agent.policy_improvement()
        print("action grid:", action_grid)
        # print("action grid flatten:", action_grid.flatten())
        action_grid = []

        for i in range(len(action_grid)):
            for j in range(len(action_grid)):
                action_grid.append(agent.policy(actions_prob=action_grid[i][j]))

        print("actions name:", action_grid)
        
        o_t, reward, status = grid.reset()
        agent.set_pos_reward(o_t, reward)        

