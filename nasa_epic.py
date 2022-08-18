import argparse
import os
import datetime

import requests

from dotenv import load_dotenv


def save_nasa_epic(dir_path, api_key):
    url = f'https://api.nasa.gov/EPIC/api/natural/images'
    parameters = {
        'api_key': api_key
        }
    response = requests.get(url, params = parameters)
    for epic_number, epic in enumerate(response.json()[:5]):
        os.makedirs(dir_path, exist_ok=True)
        filename = f'epic{epic_number}.png'
        epic_date = datetime.date.fromisoformat(epic['date'][:10]).strftime('%Y/%m/%d')
        epic_image = epic['image']
        epic_parameters = {
            'api_key': api_key
            }
        epic_response = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_image}.png', params = epic_parameters)
        epic_response.raise_for_status()
        with open(os.path.join(dir_path, filename), 'wb') as file:
            file.write(epic_response.content)
            

def main():
    load_dotenv('.env')
    parser = argparse.ArgumentParser(
        description='скачивание картинок EPIC от NASA'
    )
    parser.add_argument('dir_path', help='введите путь к директории')
    args = parser.parse_args()
    dir_path = args.dir_path
    api_key = os.environ['API_KEY_NASA']
    return(save_nasa_epic(dir_path, api_key))


if __name__ == '__main__':
    main()
