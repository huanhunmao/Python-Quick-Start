from die import Die
import plotly.express as px

# 设置两个骰子
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 制作直方图
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)
fig.show()