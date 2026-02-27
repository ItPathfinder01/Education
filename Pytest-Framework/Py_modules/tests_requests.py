import requests, json

# url = "https://www.google.com/search?q=pytest"
# r = requests.get(url)
# print(r.text)

# url = "https://www.regres.in/api/users"
# r = requests.get(url)
# print(r.status_code)
# print(r.headers)
# # print(r.text)
# print("The type is ", type(r))
# print("Content type is ", r.headers["Content-Type"])
#
# url = "https://httpbin.org/get"
# myparams = {"key1": "value1", "key2": "value2"}
# requesturl = requests.get(url, params=myparams)
# print("The request url is ", requesturl.url)
# for key, value in requesturl.json().items():
#     print("Check it ", key, ":", value)
# print("Here what we have ",requesturl.json()["headers"]["Host"])

url = "https://httpbin.org/post"
payload = {"key1": "value1", "key2": "value2"}
headers = {"accept": "application/json", "content-type": "application/json "}
requestpost = requests.post(url, json=payload, headers=headers)
print(requestpost.url)
print(requestpost.status_code)
print(requestpost.json()["headers"])
# print(requestpost.text)

