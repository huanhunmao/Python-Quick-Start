# Slice
names = ['ppx', 'kk', 'cc']
print(names[0:2]) # ['ppx', 'kk']

print(names[1:]) # ['kk', 'cc']

# loop + slice
for name in names[1:]:
    print(name.title()) # Kk, Cc