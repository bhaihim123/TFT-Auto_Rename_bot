import aiohttp, asyncio, warnings, pytz, time, os
from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config, ADMIN
from aiohttp import web
from route import web_server
import pyrogram.utils
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999


# 🔹 USER CLIENT (4GB+ কাজ এখান দিয়ে হবে)
user = Client(
    name="user_session",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.STRING_SESSION,
    workers=200
)


# 🔹 BOT CLIENT (commands, buttons)
class Bot(Client):

    def __init__(self):
        super().__init__(
            name="Tech_freak_tamil_bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )
        self.start_time = time.time()

    async def start(self):
        await super().start()
        await user.start()   # 🔥 user client start

        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME     

        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", Config.PORT).start()     

        print(f"{me.first_name} Bot Started ✨")
        print("User session connected (4GB+ Enabled) ✅")

        for id in ADMIN:
            try:
                await self.send_message(
                    id,
                    f"<blockquote><b>{me.first_name} Started (4GB+ Enabled)</b></blockquote>"
                )
            except:
                pass

        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time_ = curr.strftime('%I:%M:%S %p')
                await self.send_message(
                    Config.LOG_CHANNEL,
                    f"**{me.mention} Restarted**\n\n"
                    f"📅 `{date}`\n⏰ `{time_}`\n"
                    f"🉐 Pyrogram `{__version__}` (Layer {layer})"
                )
            except:
                print("LOG CHANNEL ERROR")


Bot().run()
