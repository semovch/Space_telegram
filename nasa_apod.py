import argparse
import os

import requests

from my_module import split
from dotenv import load_dotenv


def save_nasa_apod(dir_path, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    parameters = {
        'count': '10',
        'api_key': api_key
        }
    response = requests.get(url, params=parameters)
    response.raise_for_status
    apods = response.json()
    for number_apod, apod in enumerate(apods):
        apod_ext = split(apod["url"])
        os.makedirs(dir_path, exist_ok=True)
        filename = f'nasa{number_apod}{apod_ext}'
        response_apod = requests.get(apod['url'])
        response_apod.raise_for_status()
        with open(os.path.join(dir_path, filename), 'wb') as file:
            file.write(response_apod.content)


def main():
    load_dotenv('.env')
    parser = argparse.ArgumentParser(
        description='скачивание картинок дня от NASA'
    )
    parser.add_argument('dir_path', help='введите путь к директории')
    args = parser.parse_args()
    dir_path = args.dir_path
    api_key = os.environ['API_KEY_NASA']
    return(save_nasa_apod(dir_path, api_key))


if __name__ == '__main__':
    main()

            




