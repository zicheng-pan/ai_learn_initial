import numpy as np
from matplotlib import pyplot as plt


def get_beans(counts):
    xs = np.random.rand(counts)
    xs = np.sort(xs)
    ys = np.zeros(counts)
    for i in range(counts):
        x = xs[i]
        yi = 0.7 * x + (0.5 - np.random.rand()) / 50 + 0.5
        if yi > 0.8:
            ys[i] = 1
    return xs, ys


xs, ys = get_beans(100)
print(xs)
print(ys)

plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

w = 0.1
b = 0.1
alpha = 0.01
z = w * xs + b
a = 1 / (1 + np.exp(-z))  # 引入sigmod函数

for _ in range(10000):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        z = w * x + b
        a = 1 / (1 + np.exp(-z))
        e = (y - a) ** 2

        deda = -2 * (y - a)
        dadz = a * (1 - a)
        dzdw = x
        dzdb = 1

        dedw = deda * dadz * dzdw
        dedb = deda * dadz * dzdb

        w = w - alpha * dedw
        b = b - alpha * dedb

plt.clf()
plt.scatter(xs, ys)
plt.xlim(0, 1)
plt.ylim(0, 1.2)
z = w * xs + b
a = 1 / (1 + np.exp(-z))
plt.plot(xs, a)
plt.show()
