import argparse
import os

import requests

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
    for apod_number, apod in enumerate(apods):
        apod_ext = os.path.splitext(apod['url'])[1]
        os.makedirs(dir_path, exist_ok=True)
        filename = f'nasa{apod_number}{apod_ext}'
        apod_response = requests.get(apod['url'])
        apod_response.raise_for_status()
        with open(os.path.join(dir_path, filename), 'wb') as file:
            file.write(apod_response.content)


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

            




