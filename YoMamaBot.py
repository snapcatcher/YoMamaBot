#!/usr/bin/env python3
import random
import telepot
import time
from datetime import datetime

bot = telepot.Bot('<your bot token here')
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance2(msg)
    
    if content_type == 'text':
        current_datetime = datetime.now().strftime('%Y%m%d-%H:%M')
        author_name = msg['from']['first_name']
        author_id = msg['from']['id']
        chat_id = msg['chat']['id']
        with open("yomama.log", "a") as myfile:
            myfile.write(current_datetime + ": " + author_name + '(' + str(author_id) + ')' + " in chat id = " + str(chat_id) + "message: " + msg['text'] + '\n')
        if msg['text'].startswith('/YoMama') or msg['text'].startswith('/yomama'):
            message = random.choice(lines)
            bot.sendMessage(msg['chat']['id'], message)
        elif msg['text'].startswith('/start'):
            message = 'Receive jokes by sending /yomama'
            bot.sendMessage(msg['chat']['id'], message)

bot.notifyOnMessage(handle_message)
print('Started listening...')

lines = open('<file directory>/jokes.txt').read().splitlines()

while True:
    time.sleep(60)
