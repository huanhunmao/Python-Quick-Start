from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3]) # 存在缺失数据  转为整数会报错
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}") # Missing data for 2021-05-04 00:00:00
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# Plot highs with a blue line
ax.plot(dates, highs, label='Highs', color='blue', linewidth=2)

# Plot lows with a red line
ax.plot(dates, lows, label='Lows', color='red', linewidth=2)

# 加阴影
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()