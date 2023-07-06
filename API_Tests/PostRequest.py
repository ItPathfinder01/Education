import requests
from payloadPetCreation import *
from utilities.configurations import *
from utilities.resources import ApiResources

config = getConfig()
create_pet_url = config["API"]["base_url"] + ApiResources.addPet

uploadImage = config["API"]["base_url"] + ApiResources.uploadPetImageByID
file = {'file': open('/Users/alexkibryk/Desktop/dog.png', 'rb')}
dowloadImageResponse = requests.post(uploadImage, files=file)

print(dowloadImageResponse.text)

# response = requests.post(
#     create_pet_url,
#     json=build_pet(330, "Tuzik"),
#     headers={"Content-Type": "application/json"}
# )
#
# print(response.json())
# response_json = response.json()
# print(type(response_json))
# # print(response_json["category"]["name"])
#
# assert response_json["category"]["name"] == "Tuzik"
# print("Name validation passed")
#
# assert 200 == response.status_code
#
# pet_id = response_json["id"]
# print(pet_id)

# delete_pet_url = config["API"]["base_url"] + ApiResources.deletePet + str(pet_id)
# response_delete = requests.delete(delete_pet_url)
# if response_delete.status_code == 200:
#     print("The pet has been adopted.")
# else:
#     print("Error deleting")


