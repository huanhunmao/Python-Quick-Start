import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# Convert the response object to a dictionary.
response_dict = r.json()

repo_dicts = response_dict['items']
print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

# Selected information about each repository:
#
# Name: public-apis
# Owner: public-apis
# Stars: 302963
# Repository: https://github.com/public-apis/public-apis
# Description: A collective list of free APIs
#
# Name: system-design-primer
# Owner: donnemartin
# Stars: 264824
# Repository: https://github.com/donnemartin/system-design-primer
# Description: Learn how to design large-scale systems. Prep for the system design interview.