from pathlib import Path
import csv

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column in enumerate(header_row):
#     print(index, column)

highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)