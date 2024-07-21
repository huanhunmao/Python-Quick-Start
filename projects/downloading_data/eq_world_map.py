from pathlib import Path
import json
import plotly.express as px

# 以字符串形式读取数据并转换为 Python 对象
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties'].get('mag')
    if mag is not None:  # 检查mag是否为None
        mag = float(mag)  # Convert mag to float
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        eq_title = eq_dict['properties']['title']
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        eq_titles.append(eq_title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
         color=mags,
         color_continuous_scale='Viridis',
         labels={'color':'Magnitude'},
         projection='natural earth',
         hover_name=eq_titles,
    )
fig.show()
