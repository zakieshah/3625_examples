from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from optimization_test_functions import himmelblaus_function, sharpe_ratio, ad_roi


f = himmelblaus_function

x = y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
zs = np.array(f([np.ravel(X), np.ravel(Y)]))
Z = zs.reshape(X.shape)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})



for i in range(51):  #range(len(results.allvecs) - 3):

    # https://docs.scipy.org/doc/scipy/reference/optimize.minimize-neldermead.html
    results = minimize(f, x0=[-0.27085, -0.92304], method='Nelder-Mead', bounds=[[-5, 5], [-5, 5]],
                       options={'return_all': True, 'maxiter': i})
    print(results)
    simplex = list(results.final_simplex[0])
    simplex.append(simplex[0])
    x, y = list(zip(*simplex))
    z = f(np.array([x, y]))

    plt.cla()
    ax.plot_surface(X, Y, Z, alpha=0.5, cmap='hot')
    ax.plot(x, y, z, marker='.', c='r')
    plt.title(f'iteration {i}: {results.nfev} function evals')
    print(simplex)
    plt.pause(2 if i < 4 else 0.25)

plt.show()