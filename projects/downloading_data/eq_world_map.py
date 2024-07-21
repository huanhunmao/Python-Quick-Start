from pathlib import Path
import json
import plotly.express as px

# 以字符串形式读取数据并转换为 Python 对象
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties'].get('mag')
    if mag is not None:  # 检查mag是否为None
        mag = float(mag)  # Convert mag to float
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, projection='natural earth')
fig.show()
