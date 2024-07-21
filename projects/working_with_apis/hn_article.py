import requests
import json

# 请求
url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# 格式化输出
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_dict)