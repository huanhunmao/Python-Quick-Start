# 嵌套 list
item1 = {'color': 'red'}
item2 = {'color': 'yellow'}
list = [item1, item2]
print(list) # [{'color': 'red'}, {'color': 'yellow'}]
for ls in list:
    print(ls)
# {'color': 'red'}
# {'color': 'yellow'}

# list in Dictionary
items = {
    'color': 'yellow',
    'num': ['ppx', 'cc']
}

for key, value in items.items():
    print(f'{key}-{value}')

# color-yellow
# num-['ppx', 'cc']

# Dictionary in a Dictionary
users = {
    'user1': {
        'name': 'ppx',
        'age': 18,
    },
    'user2': {
        'name': 'cc',
        'age': 16,
    }
}

for key, value in users.items():
    print(key)
    print(value)