import sys
import time

import telepot
from telepot.loop import MessageLoop


BOT = None


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        BOT.sendMessage(chat_id, msg['text'])


def run_bot(token):
    global BOT
    BOT = telepot.Bot(token)
    MessageLoop(BOT, handle).run_as_thread()
    print('Listening ...')
    # Keep the program running.
    while 1:
        time.sleep(10)


if __name__ == "__main__":
    run_bot(sys.argv[1])
