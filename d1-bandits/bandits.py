import numpy as np 
import matplotlib.pyplot as plt

class KArmBandit:
    def __init__(self, k=10):
        # TODO
        self.k = k
        self.true_mean = np.random.normal(0,1, k)

    def pull(self, arm):
        # TODO
        self.reward = np.random.normal(self.true_mean[arm], 1)
        return self.reward

class EpsilonGreedyAgent:
    def __init__(self, k = 10, epsilon = 0.1):
        # TODO
        self.estimation_q = np.zeros(k)
        self.number_n = np.zeros(k)
        self.k = k
        self.epsilon = epsilon

    def select_arm(self):
        # TODO
        x = np.random.rand()
        if x <= self.epsilon:
            arm = np.random.randint(self.k)
            return arm
        else:
            arm_max = np.argmax(self.estimation_q) #retourne le bras avec la plus grande valeur de Q(a)
            return arm_max
        
    def update(self, arm, reward):
        # TODO
        self.number_n[arm] += 1
        self.estimation_q[arm] += (1/self.number_n[arm])*(reward - self.estimation_q[arm])


if __name__ == "__main__":

    np.random.seed(456)

    tours = 1000
    bandit = KArmBandit(k=10)
    agent = EpsilonGreedyAgent(k=10, epsilon=0.1)
    rewards_history = np.zeros(tours)

    # TODO 
    for tour in range(tours):
        arm = agent.select_arm()
        reward = bandit.pull(arm=arm)
        agent.update(arm=arm, reward=reward)
        rewards_history[tour]= reward

    #recompense cumulee
    reward_recu_au_tour_t = np.cumsum(rewards_history)
    nombre_tours_ecoule = np.arange(1, tours + 1)
    cum_reward = reward_recu_au_tour_t / nombre_tours_ecoule

    regret_t = max(bandit.true_mean) - rewards_history
    regret_cum = np.cumsum(regret_t)

    print("Meilleur bras réel :", np.argmax(bandit.true_mean))
    print("Meilleur bras réel valeur:", np.max(bandit.true_mean))
    print("Meilleur bras estimé par l'agent :", np.argmax(agent.estimation_q))
    print("Convergence réussie :", np.argmax(bandit.true_mean) == np.argmax(agent.estimation_q))

    #PLot
    plt.plot(range(tours), regret_cum)
    plt.xlabel("Tour")
    plt.ylabel("Regret cumulé")
    plt.show()

    plt.plot(range(tours), cum_reward)
    plt.xlabel("Tour")
    plt.ylabel("Reward cumulé")
    plt.show()