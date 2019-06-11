# TGBot
## Custom bot for Telegram using [Telepot](https://github.com/nickoala/telepot) and [PRAW](https://github.com/praw-dev/praw)

The bot is currently in development. As of now it replies with the messages sent in the chat it participates in. It supports some
custom commands, although they are still under development.
 
Ideally, the bot will be able to butler in chats and store chat metrics while preserving user privacy. It will be able to provide
detailed information regarding user activity in the group, as well as provide some other services, such as sending memes etc.
### Current TO-DO bullet list:
* Implement personalized butlering features
* Implement a wider variety of features
* Remove obsolete code
* Migrate from telepot to a different API library (I've just noticed that it is no longer supported, so I guess it's a necessary move sometime soon)

### Setup manual
As of the time of this text being written, this bot requires 3 libraries - telepot, praw, and emoji (the last one is just for experimentation though). To get them use `pip install $name`. If you don't have [pip](https://pypi.org/project/pip/), I advise you to get it. It's cool and free.

Afterwards you have to edit the contents of pass.txt and secret.txt in order to connect to your accounts on Reddit and Telegram, respectively. You can get Telegram Bot secret by creating a bot using BotFather. It's really simple. I think that's all for now. I promise I'll make the setup easier sometime in the future. Like maybe add a single `options.ini` file to input all your data into or something. Now I'm more focused on ~~slacking~~ functionality rather than usability.

Should anyone be even remotely interested in something related to this project, you can shoot me an [email](mailto:veleth@icloud.com).

### Notes
If you wish to fork and use this bot, bear in mind that the file memegetter.py (which supplies memes from reddit) relies on a txt file
with reddit credentials and bot secrets, which for obvious reasons is not present in this repository. It's also worth noting that the bot will be personalized to accomodate the needs of the group it's made for.

Feel free to copy, modify and distribute this piece of software in any way you see fit.

**NOTE: THE LIBRARIES USED ([TELEPOT](https://github.com/nickoala/telepot) AND [PRAW](https://github.com/praw-dev/praw)) BELONG TO THEIR RESPECTIVE OWNERS**

###### 2018 Gabriel Tański
