import  matplotlib.pyplot as plt
from random_walk import RandomWalk

# 程序还会继续生成多个随机行走
while True:
    # 进行随机walk
    rw = RandomWalk()
    rw.fill_walk()

    # 绘制walk点
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break