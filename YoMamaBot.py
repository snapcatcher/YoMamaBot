#!/usr/bin/env python

import json
import requests
import sys
import os
import random 

def request(url):
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()
    else:
        return str(req.status_code)

def sendMessage(chat_id, message):
    print "sending Message = " + message
    url = base_url + 'sendMessage?chat_id=' + chat_id + '&text=' + message
    request(url)

current_directory = os.path.dirname(os.path.realpath(__file__))

lines = open(current_directory + '/jokes.txt').read().splitlines()
myline = random.choice(lines)

token = "<your bot token here>"
base_url = "https://api.telegram.org/bot" + token + "/"

chat_id = sys.argv[1]
message = sys.argv[2]

if message.startswith("/YoMama") or message.startswith("/yomama"):
    sendMessage(chat_id, myline)
elif message.startswith("/start"):
    sendMessage(chat_id, "Receive jokes by sending /yomama")
