import numpy as np
from matplotlib import pyplot as plt


def get_beans(counts):
    xs = np.random.rand(counts)
    xs = np.sort(xs)
    ys = np.array([(0.7 * x + (0.5 - np.random.rand()) / 5 + 0.5) for x in xs])
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

for _ in range(500):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        dw = 2 * x ** 2 * w + 2 * x * b - 2 * x * y
        db = 2 * b + 2 * x * w - 2 * y

        w = w - alpha * dw
        b = b - alpha * db

plt.clf()
plt.scatter(xs, ys)
plt.xlim(0, 1)
plt.ylim(0, 1.2)
y_pre = w * xs + b
plt.plot(xs, y_pre)
plt.pause(0.01)

plt.show()
