import numpy as np
np.random.seed(42)
from comp3625_examples.search_and_optimization.optimization_test_functions import sum_city_distances, city_locations
import pygad
from matplotlib import pyplot as plt


# in this lab you'll find the best locations for 3 airports servicing 20 cities. Find the locations of the 3 airports
# such that sum-of-distances from each city to it's nearest airport are minimized.
# use a genetic algorithm (in the pygad python package) to find the best locations.


# a candidate solution is a length-6 array showing the x-y coordinates of each airport: [x1, y1, x2, y2, x3, y3]
# the function sum_city_distances gives the sum of distances for a solution
sample_solution = np.array([0.1, 0.9, 0.5, 0.5, 0.8, 0.2])
sample_distance = sum_city_distances(sample_solution)
print(f"sum-of-distances for sample solution: {sample_distance}")

# visualize the sample solution
plt.scatter(city_locations[:, 0], city_locations[:, 1])
plt.scatter(sample_solution[[0, 2, 4]], sample_solution[[1, 3, 5]], marker='x', s=100, c='red')
plt.legend(['cities', 'airports'])
plt.show()


# use a genetic algorithm to find the best airport locations
# (refer to pygad_demo.py for a simple demo of how to use pygad's genetic algorithm)
# your script should use a custom crossover function: https://pygad.readthedocs.io/en/latest/utils.html#user-defined-crossover-mutation-and-parent-selection-operators
# devise a crossover operation that is appropriate for this problem. One option is an "arithmetic crossover", which
# creates a linear combination of the two parents: offspring = 0.5*parent1 + 0.5*parent2

# your code here