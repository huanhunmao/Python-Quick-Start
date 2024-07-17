def hello():
    print('hello')

hello()


# 参数
def getUser(name='cc', age=20):
    print(f'name is {name} , age is {age}')

getUser('ppx', 18) # name is ppx , age is 18

# Returning a Dictionary
def has_person(first_name, last_name):
    person = {'first': first_name,
              'last': last_name}

    return person


p = has_person('ppx', 'cc')
print(p) # {'first': 'ppx', 'last': 'cc'}


# 传递 list
def greet(names):
    for name in names:
        msg = f'hello {name}'
        print(msg)


name_list = ['ppx', 'll', 'mm', 'cc']
greet(name_list)
# hello ppx
# hello ll
# hello mm
# hello cc

