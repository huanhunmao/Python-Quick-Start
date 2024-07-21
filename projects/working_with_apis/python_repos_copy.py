import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# Convert the response object to a dictionary.
response_dict = r.json()

repo_dicts = response_dict['items']

# 检查第一个存储库
repo_dict = repo_dicts[0]
print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

# Selected information about first repository:
# Name: public-apis
# Owner: public-apis
# Stars: 302963
# Repository: https://github.com/public-apis/public-apis
# Created: 2016-03-20T23:49:42Z
# Updated: 2024-07-21T07:40:15Z
# Description: A collective list of free APIs