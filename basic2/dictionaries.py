# 类似 js 对象

# 访问值
items = {
    'color': 'yellow',
    'price': 22,
}

print(items['color']) # yellow
print(items['price']) # 22
print(items.get('color')) # yellow
print(items.get('color1')) # None

# 添加值
items['x'] = 10
items['y'] = 20
print(items) # {'color': 'yellow', 'price': 22, 'x': 10, 'y': 20}


# 修改值
items['x'] = 180
print(items['x']) # 180

# 删除
del items['x']
print(items) # {'color': 'yellow', 'price': 22, 'y': 20}