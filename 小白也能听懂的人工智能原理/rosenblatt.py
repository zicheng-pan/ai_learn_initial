from matplotlib import pyplot as plt
import numpy as np

Beans_count = 100


def get_beans(counts):
    xs = np.random.rand(counts)
    xs = np.sort(xs)
    ys = [1.2 * x + np.random.rand() / 10 for x in xs]
    return xs, ys


xs, ys = get_beans(Beans_count)
print(xs)
print(ys)

plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

w = 0.5
alpha = 0.05

# 为了更精确w，可以多此尝试迭代步长，修正权重值
for i in range(100):
    for i in range(Beans_count):
        x = xs[i]
        y_pre = w * x
        # 前面是步长
        w = (ys[i] - y_pre) * w * alpha + w

# 绘制预测线
y_pre = w * xs
plt.plot(xs, y_pre)

# 绘制豆豆点
plt.scatter(xs, ys)
plt.show()
