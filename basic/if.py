cars = ['audi', 'bmw', 'tesla', 'toyota']

for car in cars:
    if car == 'tesla':
        print(f"I will buy {car}") # I will buy tesla


print('audi' == 'Audi') # False


if 'test' != 'testing':
    print(True) # True


age=18
if age > 18:
    print('big one')
elif age == 18:
    print('just one') # just one
else:
    print('small one')