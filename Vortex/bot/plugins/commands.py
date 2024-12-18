import logging
import pytz
import time
import asyncio
from Vortex.bot import StreamBot
from datetime import datetime, date
from pyrogram import filters, Client 
from Script import script
from Config import Var
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

def get_wish():
    tz = pytz.timezone('Asia/Colombo')
    time = datetime.now(tz)
    now = time.strftime("%H")
    if now < "12":
        status = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌞"
    elif now < "18":
        status = "ɢᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ 🌗"
    else:
        status = "ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌘"
    return status

@StreamBot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    try:
        if message.from_user.id not in Var.AUTH_USERS:
            await message.reply_text(
                f"<b>ʜᴇʏ {message.from_user.first_name or 'User'}, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ. ᴄᴏɴᴛᴀᴄᴛ <a href='https://t.me/ImaxSupp0rtBot'>ɪᴍᴀx sᴜᴘᴘᴏʀᴛ</a></b>",
                disable_web_page_preview=True
            )
            return

        buttons = [[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Akimaxmovies_0")]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo="https://telegra.ph/file/2a76d5d5785e2445dbee2-e85158cd1fb6ca6be5.jpg",
            caption=script.START_TXT.format(first=message.from_user.mention, wish=get_wish()),
            reply_markup=reply_markup
        )
    except Exception as e:
        logging.error(f"Error in start command: {str(e)}")
        await message.reply_text(f"An error occurred: {str(e)}. Please try again later.")
