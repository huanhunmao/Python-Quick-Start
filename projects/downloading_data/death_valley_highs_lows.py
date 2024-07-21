from pathlib import Path
import csv
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[3]) # 存在缺失数据  转为整数会报错
    low = int(row[4])
    dates.append(current_date)