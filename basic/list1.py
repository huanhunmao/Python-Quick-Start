items = ['ppx', 'fish', 'meal']

# add list
items.append('KK')
print(items)
# ['ppx', 'fish', 'meal', 'KK']

items.insert(0, 'MM')
print(items)
# ['MM', 'ppx', 'fish', 'meal', 'KK']

# change list

items[0] = 'CC'
print(items[0])
# 'CC'


# remove 4-KK
del items[4]
print(items) # ['CC', 'ppx', 'fish', 'meal']

items.pop()
print(items) # ['CC', 'ppx', 'fish']

# 还可以这样
items.pop(1)
print(items) # ['CC', 'fish']\

# 通过名字删除
items.remove('fish')
print(items) # ['CC']

