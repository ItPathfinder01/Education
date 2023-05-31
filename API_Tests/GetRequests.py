import requests

url = "https://swapi.dev/api/planets/1/"
# url = "https://www.influencer.com/"
print(url)
result = requests.get(url)

print("Status code is " + str(result.status_code))

assert 200 == result.status_code
if result.status_code == 200:
    print("Status code is correct")
else:
    print("Status code is incorrect")
result.encoding = "utf-8"

print(result.text)