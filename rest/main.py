# conda create -n python-examples
# conda activate python-examples
# pip install requests
import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

res = requests.get(url, headers=headers)
print(f"Status: {res.status_code}")

response_dict = res.json()
print(response_dict.keys())

print("\n")

# for key, value in response_dict.items():
#     print(f"{key}: {value}")
# print("\n")

repo_dicts = response_dict["items"]
repo_dict = repo_dicts[0]
for key, value in repo_dict.items():
    print(f"{key}: {value}")
print("\n\n")
print(f"git_url: {response_dict['items'][0]['url']}")
print(f"git_url: {response_dict['items'][0]['git_url']}")
print(f"git_url: {response_dict['items'][0]['owner']}")
