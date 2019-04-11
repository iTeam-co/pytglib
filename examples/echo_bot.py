import logging
import argparse
from pytglib.client import Telegram
from pytglib.api.types import MessageText

"""
It answers "pong" if receives "ping"

Usage:
    python examples/send_message.py api_id api_hash phone
"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('api_id', help='API id')  # https://my.telegram.org/apps
    parser.add_argument('api_hash', help='API hash')
    parser.add_argument('phone', help='Phone')
    args = parser.parse_args()

    tg = Telegram(
        api_id=args.api_id,
        api_hash=args.api_hash,
        phone=args.phone,
        database_encryption_key='changeme1234',
    )
    # you must call login method before others
    tg.login()

    def new_message_handler(update):
        message_content = update.message.content
        if isinstance(message_content, MessageText) and message_content.text.lower() == "ping":
            chat_id = update.message.chat_id
            print(f'Ping has been received from {chat_id}')
            tg.functions.send_message(
                chat_id=chat_id,
                text='pong',
            )

    tg.add_message_handler(new_message_handler)
    tg.idle()  # blocking waiting for CTRL+C
