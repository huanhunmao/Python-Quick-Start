# 剩余参数分配 这个表达有点新
def build_person(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


val = build_person('ppx', 'cc', location='CG', field='PP')
print(val) # {'location': 'CG', 'field': 'PP', 'first_name': 'ppx', 'last_name': 'cc'}

