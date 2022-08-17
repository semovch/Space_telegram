import os
import random
import time
import argparse

import telegram
from dotenv import load_dotenv


def publication(directory, tg_bot_token, tg_channel_id, sleep_time):
    while True:
        images = os.listdir(directory)
        random.shuffle(images)
        for image in images:
            bot = elegram.Bot(token=tg_bot_token)
            with open(os.path.join(directory, image), 'rb') as photo_space:
                bot.send_photo(chat_id=tg_channel_id, photo=photo_space)
            time.sleep(int(sleep_time))


def main():
    load_dotenv('.env')
    parser = argparse.ArgumentParser(
        description='публикация картинок'
    )
    parser.add_argument('directory', help='введите путь к нужной директории')
    args = parser.parse_args()
    directory = args.directory
    tg_bot_token = os.environ['TG_BOT_TOKEN']
    tg_channel_id = os.environ['TG_CHANNEL_ID']
    sleep_time = os.environ['SLEEP_TIME']
    return(publication(directory, tg_bot_token, tg_channel_id, sleep_time))


if __name__ == '__main__':
    main()
