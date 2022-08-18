import argparse
import os

import requests


def fetch_spacex_last_launch(dir_path, launch_id):
    response_launch = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response_launch.raise_for_status()
    images = response_launch.json()['links']['flickr']['original']
    for image_numb, image in enumerate(images):
        image_ext = os.path.splitext(image)[1]
        os.makedirs(dir_path, exist_ok=True)
        filename = f'spacex{image_numb}{image_ext}'
        response_image = requests.get(image)
        response_image.raise_for_status()
        with open(os.path.join(dir_path, filename), 'wb') as file:
            file.write(response_image.content)


def main():
    parser = argparse.ArgumentParser(
        description='скачивание картинок'
    )
    parser.add_argument('dir_path', help='введите путь к директории')
    parser.add_argument('--launch_id', help='введите ID запуска', default='latest')
    args = parser.parse_args()
    dir_path = args.dir_path
    launch_id = args.launch_id
    return(fetch_spacex_last_launch(dir_path, launch_id))


if __name__ == '__main__':
    main()
