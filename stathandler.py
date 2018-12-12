"""

This is the code that allows (will allow) the bot to store and access statistics

"""
import os
import json
import time
import sys
import re
from pathlib import Path

def tally(msg):
    cid = msg['chat']['id']
    uid = msg['from']['id']

    uTemplate = {
        'name' : msg['from']['first_name'], #TODO: Check if the name is correct
        'id' : uid,
        'messages' : 0,
        'characters' : 0,
        'firstActivity' : time.time(),
        'recentActivity' : time.time(),
        'x' : 0,
        'd' : 0,
        'longest_xd' : 0
        #other info/media ?
    }

    gTemplate = {
        'messages' : 0,
        'characters' : 0,
        'firstActivity' : time.time(),
        'recentActivity' : time.time(),
        'x' : 0,
        'd' : 0,
        'longest_xd' : 0
        #other info/media ?
    }
    
    path = str(os.getcwd()+"/stats/"+str(cid)+"/")
    os.makedirs(path,exist_ok=True)

    f = Path(path+"stats.txt")

    #Try to get file, create it if needed
    if f.is_file():
        with open(f, "r") as jsonFile:
            people = json.load(jsonFile)
    else:
        people = {}
        people['totals'] = gTemplate

    #File accessed, get user info
    try:
        user = people[str(uid)]
    except:
        print("Creating record for "+str(uid)+" in group "+str(cid) , file=sys.stderr)
        people[uid] = uTemplate
        user = people[uid]
    totals = people['totals']
    
    #User accessed, modify entry
    user['messages'] += 1
    totals['messages'] += 1
    user['characters'] += len(msg['text'])
    totals['characters'] += len(msg['text'])
    user['recentActivity'] = msg['date']
    totals['recentActivity'] = msg['date']

    xd = re.match(r"^[xX][dD]+$", msg['text'])
    if xd is not None: #TODO: CHECK IF IT WORKS
        xd = msg['text']
        user['x'] += 1
        totals['x'] += 1
        user['d'] += len(xd)-1
        totals['d'] += len(xd)-1
        user['longest_xd'] = max(user['longest_xd'], len(xd))
        totals['longest_xd'] = max(totals['longest_xd'], len(xd))

    #Save to file
    with open(f, "w") as jsonFile:
        json.dump(people, jsonFile)


def getStats(cid):
    #Data requested
    path = str(os.getcwd()+"/stats/"+str(cid)+"/")
    f = Path(path+"stats.txt")

    if f.is_file():
        with open(f, "r") as jsonFile:
            people = json.load(jsonFile)
    else:
        return -1 #error - no such file
    
    msg = ""
    for u in people.items():
        if(u[0] == "totals"):
            msg += "<b>Totals for group:</b>\n Total messages: "+str(u[1]['messages'])+"\n Total characters: "+str(u[1]['characters'])+"\n"#expand later
        else:
            msg += "\n<b>Name: "+u[1]['name']+"</b>\nMessages: "+str(u[1]['messages'])+"\nCharacters: "+str(u[1]['characters'])+"\n"
    return msg