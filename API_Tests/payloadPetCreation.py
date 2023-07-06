def build_pet(id, dog_name):
    body = {
        "id": id,
        "category": {
            "id": 0,
            "name": dog_name
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
    }
    return body
