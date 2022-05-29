import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 50,000个点
rw = RandomWalk(50_000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
# s 表示dot_size
# ax.scatter(rw.x_values, rw.y_values, s=15)
# point_numbers表示从0到4999的list，点是逐个绘制的，前面绘制的点是浅蓝色，后面绘制的点是深蓝色
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

plt.show()
