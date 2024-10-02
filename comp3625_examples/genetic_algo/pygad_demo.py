import pygad
import numpy as np


# define some random function to use in a sample optimization problem:
# f(x) = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6
# where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7)
# we want to find inputs x that produce an output of 44

def a_function(x):
    return np.dot(x, [4,-2,3.5,5,-11,-4.7])


desired_output = 44


# define a fitness function that scores how good a given X is.
# pygad requires the fitness function to have this signature:
def fitness_func(ga_instance, solution, solution_idx):
    output = a_function(solution)
    fitness = -np.abs(output - desired_output)
    return fitness


# instantiate the GA object
# for more info on GA params: https://pygad.readthedocs.io/en/latest/pygad.html#init
# for defining your own selection, mutation, or crossover operations:
#    https://pygad.readthedocs.io/en/latest/utils.html#user-defined-crossover-mutation-and-parent-selection-operators
ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=4,
                       fitness_func=fitness_func,
                       sol_per_pop=8,
                       num_genes=6, # length of our input X
                       init_range_low=-2,
                       init_range_high=5,
                       parent_selection_type='sss',
                       crossover_type='artithmetix_xover',
                       mutation_type='random',
                       mutation_percent_genes=10)

# run and get results
ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()

# print some results
print(f"Parameters of the best solution : {solution}")
print(f"functino output for this solution: {a_function(solution)}")
print(f"Fitness value of the best solution = {solution_fitness}")
