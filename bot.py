"""

Bot - the main file
It downloads mesages from the server in a loop and processes them.

Bot requires a token, that is supposed to be the only thing in secret.txt file.

Currently, there's no better way to call it than WIP - the planned features
are as yet inexistent, the code is messy, and the program is essentially in
debug mode - it will be changed in the future, but for now almost nothing works.

Fork at your own risk.

"""

import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import memegetter
import stathandler

secret = open("secret.txt), 'r").readline()
bot = telepot.Bot(secret)
botname = "chat_metrics_bot"
#To be removed soon
birth = time.time()
bot.sendMessage(-257580042, "I AM REBORN") #Testing zone group


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    text = msg['text']
    print(content_type, chat_type, chat_id)
    if text == "/kys@"+botname and msg['date']>birth:
        bot.sendMessage(chat_id, "I die now")
        exit(0)

    elif text == "/meme@"+botname and msg['date']>birth:
        bot.sendPhoto(chat_id, memegetter.getMeme("dankmemes"))

    elif text == "/stats@"+botname and msg['date']>birth:
        bot.sendMessage(chat_id, "Not available yet. Check back later")

    elif content_type == 'text':
        stathandler.tally(msg)
        
MessageLoop(bot, handle).run_as_thread()
while True:
    time.sleep(2)

#TODO 1: Replace Active with exit(code).
#TODO 2: Make use of dictionaries for bot commands - let the message lead to a function that is to be executed thereon, instead of this barbaric elif list.