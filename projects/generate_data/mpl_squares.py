import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)

# 设置标题和标签轴
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# 设置刻度标签大小
ax.tick_params(labelsize=14)

# 设置每个轴范围
ax.axis([0, 1100, 0, 1_100_000])
# 自定义刻度标签
ax.ticklabel_format(style='plain')

plt.show()