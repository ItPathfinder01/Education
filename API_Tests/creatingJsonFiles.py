import json
import shutil

data_to_save = {
    "name": "Nabu",
    "rotation_period": "23",
    "orbital_period": "304",
    "diameter": "10465",
    "climate": "arid",
    "gravity": "1 standard",
    "terrain": "desert",
    "surface_water": "1"
}
# Открываем файл в режиме записи и сохраняем данные в формате JSON
with open('/Users/alexkibryk/Desktop/NabuFile.json', 'w') as json_file:
    json.dump(data_to_save, json_file)

# Определите путь и имя файла JSON, который вы хотите скачать
source_file = '/Users/alexkibryk/Desktop/NabuFile.json'

# Определите путь и имя файла, куда вы хотите сохранить скачанный файл
destination_file = '/Users/alexkibryk/Downloads/NabuFile.json'

# Скопируйте файл в желаемую директорию
shutil.copyfile(source_file, destination_file)
