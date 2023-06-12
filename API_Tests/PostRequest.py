import requests

url = requests.post("https://petstore.swagger.io/v2/pet", json=
{
    "id": 111,
    "category": {
        "id": 0,
        "name": "Polkan"
    },
    "name": "Sobachniki",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "GoodDog"
        }
    ],
    "status": "available"
},
                    headers={"Content-Type": "application/json"}, )
print(url.json())
response_json = url.json()
print(type(response_json))
print(response_json["category"]["name"])

assert response_json["category"]["name"] == "Polkan"
if response_json["category"]["name"] == "Polkan":
    print("Validation passed")
else:
    print("Wrong name")

assert 200 == url.status_code
