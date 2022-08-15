import argparse
import os

import requests


def fetch_spacex_last_launch(ID, dir_name):

    response_launch = requests.get(f"https://api.spacexdata.com/v5/launches/{ID}")
    response_launch.raise_for_status()
    images = json.loads(response_launch.text)['links']['flickr']['original']
    for image_numb, image in enumerate(images):
        image_ext = os.path.splitext(image)[1]
        os.makedirs(dir_name, exist_ok=True)
        filename = f'spacex{image_numb}{image_ext}'
        response_image = requests.get(image)
        response_image.raise_for_status()
        with open(os.path.join(dir_name, filename), 'wb') as file:
            file.write(response_image.content)


def main():
    parser = argparse.ArgumentParser(
        description='скачивание картинок'
    )
    parser.add_argument('dir_name', help='введите путь к директории')
    parser.add_argument('--ID', help='введите ID запуска', default="latest")
    args = parser.parse_args()
    dir_name = args.dir_name
    ID = args.ID
    return(fetch_spacex_last_launch(ID, dir_name))


if __name__ == '__main__':
    main()
