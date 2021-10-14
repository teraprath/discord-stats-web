# Discord Stats Web
A Simple Discord Webpanel working with Python [Flask](https://flask.palletsprojects.com/en/2.0.x/) and a [MySQL-Databse](https://www.mysql.com/de/). It based on the [Discord Stats Bot](https://github.com/teraprath/discord-stats-bot) but you can of course also use and implement it for your own bot.

The project serves more as a basis than a finished one. You can modify it according to your preferences.

![Image](https://i.imgur.com/diEMgmM.png)

## Installation

1. **Download** the source and upload it on your Server or PC.
2. **Setup.** If you don't know how to set up a Flask Web App on a Linux server, [this video](https://www.youtube.com/watch?v=YFBRVJPhDGY) could help you.
3. Set up your **MySQL database** and create a database (or use your existing one from your Discord bot).
4. Go to the uploaded folder in **config.py** and enter your MySQL data.
```python
# MySQL Database
host = "localhost" # Or your host
user = "root" # Or your username
password = "password" # Or your password
database = "dcstats" # Or your name
```
5. **Open** your website and here you are.

You can modify the bot as you want.

# Use with Discord Stats Bot

Download the [Discord Stats Bot](https://github.com/teraprath/discord-stats-bot) for free and have a base for your code.

![Image](https://i.imgur.com/ZX2R5Fb.png)
