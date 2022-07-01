import numpy as np

import dataset
from matplotlib import pyplot as plt

Beans_number = 100
xs, ys = dataset.get_beans(Beans_number)
print(xs)
print(ys)

plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

# w = 0.5
# w_array = np.arange(0, 3, 0.1)
# e_array = []
# for w in w_array:
#     y_pre = w * xs
#     e = np.sum((ys - y_pre) ** 2)
#     e_array.append(e)
#
# plt.plot(w_array, e_array)

# 通过正规方程来计算误差最小出的w的值，根据二元方程 - b/2a
w = np.sum(xs * ys) / np.sum(xs * xs)
print(w)

y = w * xs
plt.scatter(xs, ys)
plt.plot(xs, y)
plt.show()
