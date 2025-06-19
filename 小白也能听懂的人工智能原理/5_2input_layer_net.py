import numpy as np


def get_beans(counts):
    xs = np.random.rand(counts, 2) * 2
    ys = np.zeros(counts)
    for i in range(counts):
        x = xs[i]
        if (x[0] - 0.5 * x[1] - 0.1) > 0:
            ys[i] = 1
    return xs, ys


def get_beans2(counts):
    xs = np.random.rand(counts, 2) * 2
    ys = np.zeros(counts)
    for i in range(counts):
        x = xs[i]
        if (np.power(x[0] - 1, 2) + np.power(x[1] - 0.3, 2)) < 0.5:
            ys[i] = 1

    return xs, ys


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def show_scatter(xs, y):
    x = xs[:, 0]
    z = xs[:, 1]
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, z, y)
    plt.show()


def show_surface(x, z, forward_propgation):
    x = np.arange(np.min(x), np.max(x), 0.1)
    z = np.arange(np.min(z), np.max(z), 0.1)
    x, z = np.meshgrid(x, z)
    y = forward_propgation(x, z)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x, z, y, cmap='rainbow')
    plt.show()


def show_scatter_surface(xs, y, forward_propgation):
    x = xs[:, 0]
    z = xs[:, 1]
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, z, y)

    x = np.arange(np.min(x), np.max(x), 0.01)
    z = np.arange(np.min(z), np.max(z), 0.01)
    x, z = np.meshgrid(x, z)
    y = forward_propgation(x, z)

    ax.plot_surface(x, z, y, cmap='rainbow')
    plt.show()


m = 100
xs, ys = get_beans(m)


w1 = np.random.rand()
w2 = np.random.rand()
b = np.random.rand()

x1s = xs[:,0]
x2s = xs[:,1]

def forward_propgation(x1s, x2s):
    z = w1 * x1s + w2 * x2s + b
    a = 1 / (1 + np.exp(-z))
    return a

show_scatter_surface(xs,ys,forward_propgation)

alpha = 0.01

for _ in range(5000):
    for i in range(m):
        x = xs[i]
        y = ys[i]
        x1 = x[0]
        x2 = x[1]
        a = forward_propgation(x1, x2)
        e = (y - a) ** 2

        deda = -2 * (y - a)
        dadz = a * (1 - a)
        dzdw1 = x1
        dzdw2 = x2
        dzdb = 1

        dedw1 = deda * dadz * dzdw1
        dedw2 = deda * dadz * dzdw2
        dedb = deda * dadz * dzdb

        w1 = w1 - alpha * dedw1
        w2 = w2 - alpha * dedw2
        b = b - alpha * dedb

# show_scatter(xs, ys)
show_scatter_surface(xs,ys,forward_propgation)
# show_scatter(xs,ys)