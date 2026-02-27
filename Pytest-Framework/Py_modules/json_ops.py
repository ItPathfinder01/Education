import json

dataDict = {
    "sampleString": "Great Automation Framework",
    "sampleList": ["Good", "Better", "Best"],
    "sampleTuple": ("Python", "Pytest", "Automation"),
    "sampleObj": {"platform": "Udemy", "Valuable": True},
    "sampleInteger": 555,
    "booleanValue": True,
    "noneValue": None
}

print("Convert py dictionary to Json")
resultJson = json.dumps(dataDict, sort_keys=True, indent=4)
print(resultJson)
#
assert type(resultJson) == str

data_dict = json.loads(resultJson)
print("The type is ", type(data_dict))
with open("example.json", "r") as file:
    data = json.load(file)
    print("The result is ", data)
    print(type(data))
    assert type(data) == dict
    print(data.keys())

for key, value in data.items():
    print("Tre result is ", key, ":", value)


def validateJson(jsonStr):
    try:
        json.loads(jsonStr)
    except ValueError as err:
        return False
    return True


jsonString = '{"name": "Lina", "salary": 3000, "email": "lina3420@gmail.com"}'

isValid = validateJson(jsonString)
print("Json string passed is valid?", isValid)
