import asyncio
import time

import requests


from main import urls, make_directory



async def download(url: str):
    try:
        if not isinstance(url, str):
            raise TypeError('Тип данных должен быть строка')
        response = requests.get(url)
        start = time.time()
        with open(f"{make_directory()}/{url.split('/')[-1]}", 'wb') as file:
            file.write(response.content)
            print(f"Загрузка файла {url.split('/')[-1]} завершена! Время выполнения загрузки {((time.time() - start)*1000):.2f}мс")
    except Exception as error:
        print(error)


async def main_loop(urls):
    loop = asyncio.get_running_loop()
    task = [loop.create_task(download(url)) for url in urls]
    await asyncio.gather(*task)

if __name__ == '__main__':
    asyncio.run(main_loop(urls))