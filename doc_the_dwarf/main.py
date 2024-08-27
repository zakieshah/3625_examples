from environment import MiningGame
import numpy as np

# instantiate the game
game = MiningGame(n_mines=2)
cumulative_reward = 0

# repeatedly ask user to choose a place to mine, and execute their choice
for _ in range(50):
    choice = int(input("choose a place to mine (0 or 1): "))
    reward = game.choose_mine(choice)
    print(f"reward: {reward}, cumulative reward: {cumulative_reward}")
