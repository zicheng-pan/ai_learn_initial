from matplotlib import pyplot as plt
import numpy as np

# 梯度下降的
def get_beans(counts):
    xs = np.random.random(counts)
    xs = np.sort(xs)
    ys = np.array([1.2 * x + np.random.rand() / 10 for x in xs])
    return xs, ys


xs, ys = get_beans(100)
print(xs)
print(ys)

plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

w = 0.1
for i in range(100):
    x = xs[i]
    y = ys[i]
    # 斜率
    k = 2 * (x ** 2) * w + (- 2 * x * y)
    alpha = 0.1
    w = w - alpha * k

    y_pre = w * xs
    plt.clf()
    plt.scatter(xs, ys)
    plt.xlim(0,1)
    plt.ylim(0,1.2)
    plt.plot(xs, y_pre)
    plt.pause(0.01)
plt.show()
# plt.scatter(xs, ys)
# plt.show()
