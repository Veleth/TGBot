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
import emoji

secret = open("secret.txt", 'r').readline()
bot = telepot.Bot(secret)
botname = "chat_metrics_bot"
#To be removed soon
birth = time.time() #right now the bot replies what it sees, so this prevents it from sending old messages
#hey = emoji.emojize("Hello there, fellow humans :thumbs_up:")
bot.sendMessage(-257580042, "I rise yet again") #Testing zone group


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        text = msg['text']
        print(content_type, chat_type, chat_id, msg['text'])

        #bloom filter flush && /roll
        if text == "/kys@"+botname and msg['date']>birth:
            bot.sendMessage(chat_id, "Cya")
            exit(0)

        elif text == "/meme@"+botname and msg['date']>birth:
            bot.sendPhoto(chat_id, memegetter.getMeme(chat_id,"dankmemes"))

        elif text == "/stats@"+botname and msg['date']>birth:
            ans = stathandler.getStats(chat_id)
            bot.sendMessage(chat_id, ans, parse_mode='html')

        else:
            stathandler.tally(msg)

    #support other kinds of content
        
MessageLoop(bot, handle).run_as_thread()
while True:
    time.sleep(2)

#TODO 1: Make use of dictionaries for bot commands - let the message lead to a function that is to be executed thereon, instead of this barbaric elif list.