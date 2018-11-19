"""

This is the code that allows (will allow) the bot to store and access statistics

"""

import os
from pathlib import Path

def tally(msg):
    cid = msg['chat']['id']
    uid = msg['from']['id']
    
    path = str(os.getpwd()+"/stats/"+cid+"/")
    os.makedirs(path,exist_ok=True)
    f1 = Path(path+uid+".txt")
    f2 = Path(path+"total.txt")

    if f1.is_file():
        with open(f1, "r") as file:
            temparr = file.nextline().split('')




