import time
import random
import requests
import os
from PIL import Image
from io import BytesIO


def save_images(pattern, id, pages):
    folder_name = id
    os.makedirs(folder_name, exist_ok=True)

    for i in range(1, pages + 1):
        url = pattern.format(id, i)
        response = requests.get(url)
        time.sleep(random.uniform(1, 3))

        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            file_name = f"{i}.jpeg"
            full_path = os.path.join(folder_name, file_name)
            image.save(full_path)
            print(f"Изображение {file_name} сохранено в папке {folder_name}")
        else:
            print(f"Ошибка {response.status_code} при загрузке {url}")


id = input("Введите ID книги в библиотеке (читайте ReadME на github): ")
pages = int(input("Введите количество страниц у книги: "))


pattern = "https://viewer.rsl.ru/api/v1/document/rsl{}/page/{}"
save_images(pattern, id, pages)
