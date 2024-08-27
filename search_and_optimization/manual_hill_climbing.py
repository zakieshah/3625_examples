import matplotlib.pyplot as plt
from optimization_test_functions import himmelblaus_function
import numpy as np

x = 3.5844
state_values = {1: himmelblaus_function([x, 1])}
current_state = 1

plt.scatter(1, state_values[1], marker='o', s=50)
plt.pause(0.1)

while True:
    direction = input('explore left or right? (r/l): ')
    current_state += 0.2 if direction == 'r' else -0.2
    state_values[current_state] = himmelblaus_function([x, current_state])
    state_values = dict(sorted(state_values.items()))

    plt.cla()
    plt.plot(state_values.keys(), state_values.values())
    plt.scatter(current_state, state_values[current_state], marker='X', s=50, c='orange')
    plt.pause(0.1)