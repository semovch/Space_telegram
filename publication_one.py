import os
import random
import argparse

import telegram
from dotenv import load_dotenv
load_dotenv('.env')


def publication_one(directory, image):
    if image is None:
        images = os.listdir(directory)
        random.shuffle(images)
        bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
        bot.send_photo(chat_id='@testchanelSemOvch', photo=open(os.path.join(directory, images[1]), 'rb'))
    else:
        bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
        bot.send_photo(chat_id='@testchanelSemOvch', photo=open(os.path.join(directory, image), 'rb'))
    
    
def main():
    parser = argparse.ArgumentParser(
        description='публикация картинки'
    )
    parser.add_argument('directory', help='введите путь к нужной директории')
    parser.add_argument('--image', help='введите название картинки')
    args = parser.parse_args()
    directory = args.directory
    image = args.image
    return(publication_one(directory, image))
    
    
if __name__ == '__main__':
    main()        
