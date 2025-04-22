import requests
import json

# all_repo_noauth = "https://api.github.com/repositories"
# resp2 = requests.get(all_repo_noauth)
# print(resp2.text)

session = requests.Session()
session.auth = authentication = ('alexarmy1607@gmail.com', 'env')
user_repos_url = "https://api.github.com/user/repos"


githab_response = session.get(user_repos_url, allow_redirects=False, timeout=1)
response_data = json.loads(githab_response.text)
print(response_data)
print(githab_response.status_code)

for pair in response_data:
    print(pair["full_name"])

