from operator import itemgetter

import requests

#  请求结构是一堆 id
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 用这个 id 请求新的 url 获取新的数据
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    # print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # 为每篇文章建立一个字典
    submission_dict = {
        'title': response_dict['title'],
        'hn_link':  f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Status code: 200
# id: 31390506    status: 200
# id: 31389893    status: 200
# id: 31390742    status: 200
# --snip--
#
# Title: Fly.io: The reclaimer of Heroku's magic
# Discussion link: https://news.ycombinator.com/item?id=31390506
# Comments: 134
#
# Title: The weird Hewlett Packard FreeDOS option
# Discussion link: https://news.ycombinator.com/item?id=31389893
# Comments: 64
# ...