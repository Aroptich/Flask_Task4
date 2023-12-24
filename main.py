import random
import time

import requests
import os
from datetime import datetime

from threads import *
from multyproces import *

urls = ['https://cs14.pikabu.ru/post_img/2022/08/02/3/1659407427123535691.jpg',
        'https://zagony.ru/admin_new/foto/2022-12-2/1669983568/kartinki-so-smyslom-15-foto_1.jpg',
        'https://amiel.club/uploads/posts/2022-03/1647722251_1-amiel-club-p-krasivie-i-neobichnie-kartinki-1.jpg',
        'https://www.donuzlav.com/photo/images/photki14.jpg',
        'https://images.wallpapershq.com/wallpapers/8083/wallpaper_8083_1080x1920.jpg']


def download(url: str):
    try:
        # if len(url) == 0:
        #     raise Exception('Список ссылок пуст')
        # if not isinstance(url, list):
        #     raise TypeError('Тип передаваемых данных должен быть список')
        # for item in url:
        if not isinstance(url, str):
            raise TypeError('Тип данных должен быть строка')
        response = requests.get(url)
        start = time.time()
        with open(f"{make_directory()}/{url.split('/')[-1]}", 'wb') as file:
            file.write(response.content)
            time.sleep(random.randint(1,3))
            print(f"Загрузка файла {url.split('/')[-1]} завершена! Время выполнения загрузки {(time.time() - start):.2f}мс")
    except Exception as error:
        print(error)


def make_directory(dir_name='Download') -> str:
    if dir_name not in os.listdir(os.getcwd()):
        os.mkdir(os.path.join(os.getcwd(), dir_name))
    return dir_name


if __name__ == '__main__':
    # thread(download, urls)
    multproc(download, urls)
