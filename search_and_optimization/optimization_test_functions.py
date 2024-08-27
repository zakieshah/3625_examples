import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


def himmelblaus_function(input_vector) -> float:
    x, y = input_vector
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def ad_campaign_profit(input_vector):
    input_vector = input_vector * 7 - 3
    x, y, z, _ = input_vector
    r = 60 - (np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1) + z/10
    return -r


city_locations = np.random.random((20, 2))


def sum_city_distances(input_vector) -> float:
    input_vector = input_vector.reshape((-1, 2))
    dists = cdist(input_vector, city_locations, metric='minkowski')
    return dists.sum()


if __name__ == '__main__':

    # from scipy.optimize import minimize
    # result = minimize(ad_campaign_profit, x0=[0.5, 0.5, 0.5, 0], bounds=[[0, 1]]*4, method='Nelder-Mead')
    # print(result)
    # exit()


    x = y = np.arange(0, 1, 0.05)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros(X.shape)
    for i in range(X.shape[0]):
        for j in range(Y.shape[1]):
            Z[i, j] = sum_city_distances(np.array([X[i, j], Y[i, j]]))



    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, Z, alpha=0.5, cmap='hot')
    stem = ax.scatter(city_locations[:, 0], city_locations[:, 1])
    plt.legend(['sum of distances', 'cities'])
    ax.set_xlabel('location (x)')
    ax.set_ylabel('location (y)')
    ax.set_zlabel('sum of distances')
    plt.show()
