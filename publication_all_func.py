import os
import random
import time
import argparse

import telegram
from dotenv import load_dotenv
load_dotenv('.env')


def publication(directory):
    while True:
        images = os.listdir(directory)
        random.shuffle(images)
        for image in images:
            bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
            bot.send_photo(chat_id='@testchanelSemOvch', photo=open(os.path.join(directory, image), 'rb'))
            time.sleep(int(os.environ['SLEEP_TIME']))


def main():
    parser = argparse.ArgumentParser(
        description='публикация картинок'
    )
    parser.add_argument('directory', help='введите путь к нужной директории')
    args = parser.parse_args()
    directory = args.directory
    return(publication(directory))
    
    
if __name__ == '__main__':
    main()        

