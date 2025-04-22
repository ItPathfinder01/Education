import requests
import json
import shutil

# url = "https://swapi.dev/api/planets/1/"
# # url = "https://www.influencer.com/"
# print(url)
# result = requests.get(url)
#
# print("Status code is " + str(result.status_code))
#
# assert 200 == result.status_code
# if result.status_code == 200:
#     print("Status code is correct")
# else:
#     print("Status code is incorrect")
# result.encoding = "utf-8"
#
# print(result.text)

response = requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "Rahul Shetty2"},)

# dict_response = (json.loads(response.text))
# print(dict_response)
# print(dict_response[0]["aisle"])

json_response = response.json()
print(type(json_response))
print(json_response[0]["aisle"])
assert response.status_code == 200
if response.status_code == 200:
    print("Status code is correct")
else:
    print("Status code is incorrect")

# print(response.headers)

assert response.headers["Content-type"] == "application/json;charset=UTF-8"
if response.headers["Content-type"] == 'application/json;charset=UTF-8':
    print ("Content-type is correct")
else:
    print("Incorrect content-type")
