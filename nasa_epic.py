import argparse
import os
import datetime

import requests
import json

from dotenv import load_dotenv


def save_nasa_epic(dir_path, api_key):
    url = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}"
    response = requests.get(url)
    response_json = json.loads(response.text)
    for number_epic, epic in enumerate(response_json[:5]):
        os.makedirs(dir_path, exist_ok=True)
        filename = f'epic{number_epic}.png'
        date_epic = datetime.date.fromisoformat(epic['date'][:10]).strftime("%Y/%m/%d")
        image_epic = epic["image"]
        response_epic = requests.get(f"https://api.nasa.gov/EPIC/archive/natural/{date_epic}/png/{image_epic}.png?api_key={api_key}")
        response_epic.raise_for_status()
        with open(os.path.join(dir_path, filename), 'wb') as file:
            file.write(response_epic.content)
            

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
