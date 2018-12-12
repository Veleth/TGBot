"""

This file is responsible for memeGetter, the functionality
that accesses reddit using PRAW API and downloads memes.

To work properly it requires a pass.txt file with reddit credentials:
client id in the first line,
client secret in the second line,
password in the third line,
username in the fourth line.

The program lacks OAuth integration, so make sure the account is not secured with 2FA.

"""

import praw
from urllib import request
from bloom import Bloom
import os
from pathlib import Path

with open('pass.txt', 'r') as f:
    s1 = f.readline()[:-1] #\n character
    s2 = f.readline()[:-1]
    s3 = f.readline()[:-1]
    s4 = f.readline()
    if s4[-1] == "\n":
        s4 = s4[:-1]

reddit = praw.Reddit(client_id=s1, client_secret=s2,
                     password=s3,
                     user_agent='Memegetter by /u/'+s4,
                     username=s4)

def getMeme(cid,sub):
    path = str(os.getcwd()+"/stats/"+str(cid)+"/")
    os.makedirs(path,exist_ok=True)

    f = Path(path+"bloom.txt")
    print(f)
    filter = Bloom()
    if f.is_file():
        file = open(f, "r")
        filter.getTable(file)
        file.close()
    else:
        file = open(f, "w+")

    global reddit
    for s in reddit.subreddit(sub).hot():
        if not filter.find(str(s)) and s.is_reddit_media_domain:
            filter.insert(str(s))
            with open(f, "w") as file:
                filter.writeTable(file)
            break
    request.urlretrieve(s.url, "temp.jpg")
    return open("temp.jpg", "rb")

#getMeme(123,"dankmemes")