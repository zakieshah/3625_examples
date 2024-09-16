from environment import MiningGame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# instantiate the game
game = MiningGame(n_mines=2)
cumulative_reward = 0

# local variables
perceived_values = [1, 1]
alpha = 0.05

# setup a dataframe to store perceived values over time
perceptions = pd.DataFrame()

# repeatedly ask user to choose a place to mine, and execute their choice
for step in range(150):
    # choice = int(input("choose a place to mine (0 or 1): "))
    # choice = np.argmax(perceived_values)
    choice = np.random.choice([0, 1])
    reward = game.choose_mine(choice)
    print(f"reward: {reward}, cumulative reward: {cumulative_reward}")
    perceived_values[choice] += alpha * (reward - perceived_values[choice])
    perceptions.loc[step, 'perceived_0'] = perceived_values[0]
    perceptions.loc[step, 'perceived_1'] = perceived_values[1]

p_rewards = np.array(game.reward_probabilities)
print(p_rewards + (1-p_rewards) * -1)
perceptions[['true_0', 'true_1']] = p_rewards + (1-p_rewards) * -1

plt.close()
plt.plot(perceptions['perceived_0'], 'r')
plt.plot(perceptions['perceived_1'], 'b')
plt.plot(perceptions['true_0'], 'r:')
plt.plot(perceptions['true_1'], 'b:')
plt.legend(['perceived value 0', 'perceived value 1', 'true value 0', 'true value 1'])
plt.show()
