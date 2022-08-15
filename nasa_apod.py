import argparse
import os

import requests
import json

from my_module import split
from dotenv import load_dotenv


def save_nasa_apod(dir_name, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    parameters = {
        'count': '10',
        'api_key': api_key
        }
    response = requests.get(url, params=parameters)
    response.raise_for_status
    apods = json.loads(response.text)
    for number_apod, apod in enumerate(apods):
        apod_ext = split(apod["url"])
        os.makedirs(dir_name, exist_ok=True)
        filename = f'nasa{number_apod}{apod_ext}'
        response_apod = requests.get(apod['url'])
        response_apod.raise_for_status()
        with open(os.path.join(dir_name, filename), 'wb') as file:
            file.write(response_apod.content)


def main():
    load_dotenv('.env')
    parser = argparse.ArgumentParser(
        description='скачивание картинок дня от NASA'
    )
    parser.add_argument('dir_name', help='введите путь к директории')
    args = parser.parse_args()
    dir_name = args.dir_name
    api_key = os.environ['API_KEY_NASA']
    return(save_nasa_apod(dir_name))


if __name__ == '__main__':
    main()

            




