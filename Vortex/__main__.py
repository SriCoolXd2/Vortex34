import os
import sys
import time
import pytz
import glob
import logging
import asyncio
import logging
import importlib
from Config import Var
from aiohttp import web
from pytz import timezone
from pyrogram import idle
from Vortex.bot import StreamBot
from pyrogram.raw.all import layer
from datetime import date, datetime
from Vortex.server import web_server
from pyrogram import Client, __version__
from Vortex.bot.clients import initialize_clients

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

StreamBot.start()
loop = asyncio.get_event_loop()

async def start_services():
    bot_info = await StreamBot.get_me()
    StreamBot.username = bot_info.username
    await initialize_clients()
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if Var.ON_HEROKU else Var.BIND_ADRESS
    await web.TCPSite(app, bind_address, Var.PORT).start()
    curr = datetime.now(timezone("Asia/Kolkata"))
    date = curr.strftime('%d %B, %Y')
    time = curr.strftime('%I:%M:%S %p')
    await StreamBot.send_message(Var.LOG_CHANNEL, f"<b>{bot_info.mention} ɪs ʀᴇsᴛᴀʀᴛᴇᴅ !!\n\n<blockquote>⏰ ᴅᴀᴛᴇ : `{date}`\n📅 ᴛɪᴍᴇ : `{time}`\n🌐 ᴛɪᴍᴇᴢᴏɴᴇ : `Aisa/Kolkata`\n\n🉐 ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : `V{__version__}`\n📌 ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `V3.13.1`</blockquote></b>")  
    print(f"Vortex Stream Bot Started......⚡️⚡️⚡️")
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')
