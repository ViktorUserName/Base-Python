import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def dowload_manga_images(url, folder='manga_images'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print('Ошибка загрузки странцы')
        return

    soap = BeautifulSoup(response.text, 'html.parser')


    images = soap.find_all('img')

    for i, img in enumerate(images):
        img_url = img.get('src')
        if img_url:
            img_url = urljoin(url, img_url)

            img_data = requests.get(img_url).content

            img_name = f'{i+1}.jpg'
            img_path = os.path.join(folder, img_name)

            with open( img_path, 'wb') as f:
                f.write(img_data)

                print(f'Сохранено: {img_name}')


dowload_manga_images('https://www.mangaread.org/manga/return-of-the-mad-demon/chapter-1/')
