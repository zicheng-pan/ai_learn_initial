import numpy as np
from matplotlib import pyplot as plt


def get_beans(counts):
    xs = np.random.rand(counts) * 2
    xs = np.sort(xs)
    ys = np.zeros(counts)
    for i in range(counts):
        x = xs[i]
        yi = 0.7 * x + (0.5 - np.random.rand()) / 50 + 0.5
        if yi > 0.8 and yi < 1.4:
            ys[i] = 1

    return xs, ys


def sigmod(z):
    return 1 / (1 + np.exp(-z))


xs, ys = get_beans(100)
print(xs)
print(ys)

plt.scatter(xs, ys)

w11_1 = np.random.rand()
b1_1 = np.random.rand()

w12_1 = np.random.rand()
b2_1 = np.random.rand()

w11_2 = np.random.rand()
w21_2 = np.random.rand()
b1_2 = np.random.rand()


def forward_propgation(xs):
    z1_1 = w11_1 * xs + b1_1
    a1_1 = sigmod(z1_1)
    z2_1 = w21_2 * xs + b2_1
    a2_1 = sigmod(z2_1)
    z1_2 = w11_2 * a1_1 + w21_2 * a2_1 + b1_2
    a1_2 = sigmod(z1_2)
    return a1_2, z1_2, a2_1, z2_1, a1_1, z1_1


a1_2, z1_2, a2_1, z2_1, a1_1, z1_1 = forward_propgation(xs)
plt.plot(xs, a1_2)

plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

alpha = 0.03

for _ in range(5000):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        # 先来一次前向传播得到结果a1_2然后计算误差e
        a1_2, z1_2, a2_1, z2_1, a1_1, z1_1 = forward_propgation(x)
        e = (y - a1_2) ** 2

        deda1_2 = -2 * (y - a1_2)
        da1_2dz1_2 = a1_2 * (1 - a1_2)
        dz1_2dw11_2 = a1_1
        dz1_2dw21_2 = a2_1
        dz1_2db1_2 = 1

        dedw11_2 = deda1_2 * da1_2dz1_2 * dz1_2dw11_2
        dedw21_2 = deda1_2 * da1_2dz1_2 * dz1_2dw21_2
        dedb1_2 = deda1_2 * da1_2dz1_2 * dz1_2db1_2

        # 再向上一层求导，链式法则，除了对参数求导得到调参的步长，再对上一级的变量求导，继续反向传播用
        dz1_2da1_1 = w11_2
        dz1_2da2_1 = w21_2

        da1_1dz1_1 = a1_1 * (1 - a1_1)
        dz1_1dw11_1 = x
        dz1_1db1_1 = 1

        dedw11_1 = deda1_2 * da1_2dz1_2 * dz1_2da1_1 * da1_1dz1_1 * dz1_1dw11_1
        dedb1_1 = deda1_2 * da1_2dz1_2 * dz1_2da1_1 * da1_1dz1_1 * dz1_1db1_1

        da2_1dz2_1 = a2_1 * (1 - a2_1)
        dz2_1dw12_1 = x
        dz2_1db2_1 = 1

        dedw12_1 = deda1_2 * da1_2dz1_2 * dz1_2da2_1 * da2_1dz2_1 * dz2_1dw12_1
        dedb2_1 = deda1_2 * da1_2dz1_2 * dz1_2da2_1 * da2_1dz2_1 * dz2_1db2_1

        w11_1 = w11_1 - alpha * dedw11_1
        b1_1 = b1_1 - alpha * dedb1_1
        w12_1 = w12_1 - alpha * dedw12_1
        b2_1 = b2_1 - alpha * dedb2_1
        w21_2 = w21_2 - alpha * dedw21_2
        b1_2 = b1_2 - alpha * dedb1_2
        w11_2 = w11_2 - alpha * dedw11_2


    if _ % 100 == 0:
        plt.clf()
        plt.scatter(xs, ys)
        a1_2, z1_2, a2_1, z2_1, a1_1, z1_1 = forward_propgation(xs)
        plt.plot(xs, a1_2)
        plt.pause(0.01)

plt.show()
