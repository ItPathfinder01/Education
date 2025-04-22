from bs4 import BeautifulSoup
import requests

# url = "https://dev-b.influencer.com/admin/#/dashboard"
# authentication = ('admin@influencer.com', 'm45ExkrUd8')
# result = requests.get(url, auth=authentication)
#
# assert 200 == result.status_code
# if result.status_code == 200:
#     print("Status code is 200 - correct")
# else:
#     print("Status code is incorrect")
# result.encoding = "utf-8"
#
# html_doc = BeautifulSoup(result.text, 'html.parser')
# formatted_html = html_doc.prettify()
# print(formatted_html)
# print(result.text)

user_repos_url = "https://api.github.com/user/repos"
# all_repo_noauth = "https://api.github.com/repositories"
authentication = ('alexarmy1607@gmail.com', 'Siemens1234qa')

# resp2 = requests.get(all_repo_noauth)
# print(resp2.text)

githab_response = requests.get(repos_url, auth=authentication)
print(githab_response.text)