from scipy.optimize import dual_annealing, minimize
import numpy as np
import matplotlib.pyplot as plt
from optimization_test_functions import himmelblaus_function


# method = 'L-BFGS-B'     # a gradient-descent approach
method = 'annealing'      # simulated annealing


test_point_log = []


def himmelblaus_function_with_log(input_vector):
    test_point_log.append(input_vector)
    return himmelblaus_function(input_vector)


x = y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
zs = np.array(himmelblaus_function([np.ravel(X), np.ravel(Y)]))
Z = zs.reshape(X.shape)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

if method == 'annealing':
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html
    results = dual_annealing(himmelblaus_function_with_log, x0=[-0.2708, -0.92304], bounds=[(-5, 5)]*2, maxiter=50, seed=42, no_local_search=True,
                             initial_temp=10, restart_temp_ratio=1e-10)

elif method == 'L-BFGS-B':
    results = minimize(himmelblaus_function_with_log, x0=[-0.2708, -0.92304], bounds=[(-5, 5)]*2, method='L-BFGS-B')


print(results)
print(len(test_point_log), test_point_log)

for i in range(len(test_point_log)):
    x, y = test_point_log[i]
    z = himmelblaus_function(test_point_log[i])

    plt.cla()
    ax.plot_surface(X, Y, Z, alpha=0.5, cmap='hot')
    ax.plot(x, y, z, marker='.', c='r')
    plt.title(f'{method}\n{i} function evals')
    plt.pause(1 if i < 2 else 0.05)

plt.show()