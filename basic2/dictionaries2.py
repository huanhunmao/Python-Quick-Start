# 遍历
items = {
    'color': 'yellow',
    'price': 22,
}

for key, value in items.items():
    print(f'{key}-{value}')

# color-yellow
# price-22

# 遍历 keys
for keys in items.keys():
    print(keys) # color price

# 遍历 value
for value in items.values():
    print(value) # yellow 22

# sorted()
print(sorted(items.keys())) # ['color', 'price']