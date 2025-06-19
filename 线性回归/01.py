import numpy as np
from matplotlib import pyplot as plt


# generate Data
def get_beans(counts):
    xs = np.sort(np.random.random(counts))
    xs = np.sort(xs)
    ys = np.array([1.5 * x + np.random.rand() / 10 for x in xs])

    # 这里假设数据有负数
    xs = xs * -1
    ys = ys * -1
    return xs, ys

count = 100
x, y = get_beans(count)


# 预测值y_pre = w*x+b 这里只预测w
def pre_Forward(x, y, w, alpha):
    for index in range(count):
        y_pre = w * x[index]        #前向传播
        loss = y[index] - y_pre
        w = w + loss * alpha * x[index]   #反向传播  这里采用了x这个值的符号来学习，x为负，误差为负就增加
        draw(x, y, calc_pre_w(x, w))


# 这里将每一个w训练变化的过程计算执行可以动态的展示当前w的直线是越来越趋近于真实值的趋势的
def calc_pre_w(x, w):
    return x * w


def draw(x, y, y_pre, method=plt.scatter):
    # 画线
    method = plt.plot # 正常情况下是拟合，但是如果直接用这个plot这个就是过拟合
    plt.clf()

    plt.title("Size-Toxicity Function", fontsize=12)
    plt.xlabel("Bean Size")
    plt.ylabel("Toxicity")
    plt.scatter(x, y)

    method(x, y_pre)
    plt.pause(0.01)


pre_Forward(x, y, 0.5, 0.1)

plt.show()
