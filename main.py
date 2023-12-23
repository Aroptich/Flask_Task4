import time

import requests
import os
from datetime import datetime

urls = ['https://cs14.pikabu.ru/post_img/2022/08/02/3/1659407427123535691.jpg',
        'https://zagony.ru/admin_new/foto/2022-12-2/1669983568/kartinki-so-smyslom-15-foto_1.jpg']


def download(url: list[str]):
    try:
        if len(url) == 0:
            raise Exception('Список ссылок пуст')
        if not isinstance(url, list):
            raise TypeError('Тип передаваемых данных должен быть список')
        for item in url:
            if not isinstance(item, str):
                raise TypeError('Тип данных должен быть строка')
            response = requests.get(item)
            start = time.time()
            with open(f"{make_directory()}/{item.split('/')[-1]}", 'wb') as file:
                file.write(response.content)
                print(f"Загрузка файла {item.split('/')[-1]} завершена! Время выполнения загрузки {(time.time() - start)}мс")
    except Exception as error:
        print(error)


def make_directory(dir_name='Download') -> str:
    if dir_name not in os.listdir(os.getcwd()):
        os.mkdir(os.path.join(os.getcwd(), dir_name))
    return dir_name


if __name__ == '__main__':
    download(url=urls)
