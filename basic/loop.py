cars = ['bmw', 'audi', 'tesla', 'toyota']

for car in cars:
    print(car)
    print(f'{car} is good')

print('loop out')

# range
for value in range(1, 5):
    print(value) # 1-4

# list range
num = list(range(1,5))
print(num) # [1, 2, 3, 4]

num1 = list(range(1,10, 2))
print(num1) # [1, 3, 5, 7, 9]


# list  range append
ls = []
for value in range(1, 11):
    new_value = value ** 2
    ls.append(new_value)

print(ls) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]