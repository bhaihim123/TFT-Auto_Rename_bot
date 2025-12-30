import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 



# Fetch initial admin list
ADMIN = [7575574860]  # TemporLoad admins when the bot starts

TOKEN_VERIFY=False
API = environ.get("API", "5a7508a173d6462e4cd4b723766b92541c389a6b") # shortlink api
URL = environ.get("URL", "arolinks.com") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/+Gt55OVP7VTAyNmNl") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "Ghjjjoooo_bot") # bot username without @
VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.
USER_LIMIT_TIME = int(os.environ.get("USER_LIMIT_TIME", "1"))#enter time based on hours

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "30775734")
    API_HASH  = os.environ.get("API_HASH", "b7d8ccaedaac68008d12e3ee7f5ae867")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8566325870:AAFQfTlvFz8C60kZLJCFdFKcvRIGJxMS5TY") 
    STRING_SESSION = "AQHVmbYArKcX6tczjdHEkKWYJpKdgJ33JXRLHVH83E1DGjbUwlekuO7B7kQnEWxnscpPWXESnbEZt-G16lfMO9PtfkB5dFTY8JwfmmSKGZ7ZI83059-yTgsbHhIQ3BTr4yaWI86tCxVP9wj4aT0vTiPHmvXjGZuNw1QbcBcYLGnI_2rhQNMfBuP7UGWkzdnGyYERI6XrFqdiAyurkzgiVr7ccp2uhex65lKLyD2lz0OfXZWbu1CCuavGIK6-0g8rDchmnpgxHb2gE4SIihEnEjb-hX0WyIojvViODvShGJDjJQrT-dMT79PfyJftPATOwMTLUc4sl_B-C9NQ9Y6qnZEQSzLIIgAAAAHDihlMAA"
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://bhaihim863:ds5P8DrfeVT5vkEi@cluster0.oacffum.mongodb.net/?appName=Cluster0")
    PORT = os.environ.get("PORT", "8050")
    OWNER = int(os.environ.get("OWNER", "7575574860"))
    PRIVATE_USE = False #If Bot is private use set True otherwise False
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://files.catbox.moe/ufzpkn.jpg")
    
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', "Ronituniverse").split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003569385777" ))
    DUMB_CHANNEL = os.environ.get("DUMB_CHANNEL", "")
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 👋 

<blockquote>➻ This Is An Advanced Auto rename Bot.

➻ Using This Bot You Can Able to Rename Your Files one by one or multi.

➻ You Can Also Select the file type is need to upload.

➻ This Bot is only for Admin use other can use with low limitation </blockquote>

<blockquote><b>Bot Is Made By :</b> @Tech_Freak_Tamil</blockquote>"""

    ABOUT_TXT = f"""<blockquote><b>😈 My Name :</b> <a href='https://t.me/Tech_Freak_Tamil'>Auto Renamer bot ⚡</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Tech_Freak_Tamil'>TFT BOTS</a>
<b>🛡️ Disscussion :</b> <a href='https://t.me/+ov2l_dY_8jA3MGVl'>TFT Discussion</a></blockquote>
    
<blockquote><b>😈 Bot Made By :</b> <a href='https://t.me/+ov2l_dY_8jA3MGVl'>TFT Discussion</a></blockquote>"""

    HELP_TXT = """<blockquote>
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /settings - Set Queue, Upload type and metadata 
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

</blockquote>"""

    PROGRESS_BAR = """\n<blockquote>
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
</blockquote>"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `Now off❌`
"""


    SEND_METADATA = """<blockquote><b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @Tech_Freak_Tamil</code>

💬 For Any Help Contact @Tech_Freak_Tamil
</blockquote>"""


# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @Tech_freak_tamil
# Developer @devilo7


