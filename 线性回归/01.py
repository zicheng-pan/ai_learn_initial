import numpy as np
from matplotlib import pyplot as plt


# generate Data
def get_beans(counts):
    xs = np.random.random(counts)
    xs = np.sort(xs)
    ys = np.array([10 * x + np.random.rand() / 10 for x in xs])
    return xs, ys


x, y = get_beans(100)


# 预测值y_pre = w*x+b 这里只预测w
def pre_Forward(x, y, w, alpha):
    for item in x:
        y_pre = w * item
        loss = y - y_pre
        w = w + loss * alpha
        draw(x, y, calc_pre_w(x, w))


# 这里将每一个w训练变化的过程计算执行可以动态的展示当前w的直线是越来越趋近于真实值的趋势的
def calc_pre_w(x, w):
    return x * w


def draw(x, y, y_pre, method=plt.scatter):
    # 画线
    method = plt.plot
    plt.clf()

    plt.title("Size-Toxicity Function", fontsize=12)
    plt.xlabel("Bean Size")
    plt.ylabel("Toxicity")
    plt.scatter(x, y)

    method(x, y_pre)
    plt.pause(0.01)


pre_Forward(x, y, 0.5, 0.1)

plt.show()
