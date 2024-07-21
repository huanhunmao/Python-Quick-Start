from  pathlib import Path
import json

# 以字符串形式读取数据并转换为 Python 对象
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# # 创建一个更可读的数据文件版本
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4 )
# path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(lons[:5])
print(lats[:5])
# [-150.7585, -153.4716, -148.7531, -159.6267, -155.248336791992]
# [61.7591, 59.3152, 63.1633, 54.5612, 18.7551670074463]