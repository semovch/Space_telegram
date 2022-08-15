import os
import random
import argparse

import telegram
from dotenv import load_dotenv


def publication_one(directory, image):
    if image:
        bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
        bot.send_photo(chat_id=os.environ['TG_CHANNEL_ID'], photo=open(os.path.join(directory, image), 'rb'))
    else:
        images = os.listdir(directory)
        random.shuffle(images)
        bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
        bot.send_photo(chat_id=os.environ['TG_CHANNEL_ID'], photo=open(os.path.join(directory, images[1]), 'rb'))
    
def main():
    load_dotenv('.env')
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
