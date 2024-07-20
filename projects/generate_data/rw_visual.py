import  matplotlib.pyplot as plt
from random_walk import RandomWalk

# 进行随机walk
rw = RandomWalk()
rw.fill_walk()

# 绘制walk点
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()