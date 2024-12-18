import os
import asyncio
from asyncio import TimeoutError
from Vortex.bot import StreamBot
from Vortex.utils.human_readable import humanbytes
from Config import Var
from urllib.parse import quote_plus
from pyrogram.enums import ParseMode
from pyrogram import filters, enums, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Vortex.utils.file_properties import get_name, get_hash, get_media_file_size

msg_text = """<b>ғɪʟᴇ ɴᴀᴍᴇ : {}

ᴅᴏᴡɴʟᴏᴀᴅ: <code>{}</code>

ɴᴏᴛᴇ : ʟɪɴᴋ ᴡᴏɴ'ᴛ ᴇxᴘɪʀᴇ ᴛɪʟʟ ɪ ᴅᴇʟᴇᴛᴇ</b>"""

@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio | filters.photo), group=4)
async def private_receive_handler(c: Client, m: Message):
    try:
        if m.from_user.id not in Var.AUTH_USERS:
            await message.reply_text(
                f"<b>ʜᴇʏ {message.from_user.first_name}, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ. ᴄᴏɴᴛᴀᴄᴛ <a href='https://t.me/ImaxSupp0rtBot'>ɪᴍᴀx sᴜᴘᴘᴏʀᴛ</a></b>",
                disable_web_page_preview=True
            )
            return            
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        await log_msg.reply_text(
            text=f"<b>RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ : [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nUꜱᴇʀ ɪᴅ : `{m.from_user.id}`</b>",
            disable_web_page_preview=True,
            quote=True
        )
        await m.reply_text(
            text=msg_text.format(get_name(log_msg), online_link),
            quote=True,
            disable_web_page_preview=True,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ', url=online_link)
                ]
            ])
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`",
            disable_web_page_preview=True
        )

@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo) & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    try:
        if broadcast.chat.id not in Var.AUTH_CHATS and broadcast.chat.id not in Var.LOG_CHANNEL:
            await bot.send_message(
                chat_id=broadcast.chat.id,
                text="ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ. ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ɪᴍᴀx sᴜᴘᴘᴏʀᴛ ғᴏʀ ᴀssɪsᴛᴀɴᴄᴇ."
            )
            return

        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        original_caption = broadcast.caption or "No Caption"
        updated_caption = f"<b>{original_caption}\n\n<a href='{online_link}'>👉 Download Link</a></b>"
        await log_msg.reply_text(
            text=f"**Channel Name:** `{broadcast.chat.title}`\n**CHANNEL ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** {online_link}",
            quote=True
        )
        await bot.edit_message_caption(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            caption=updated_caption,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ", url=online_link)]]
            )
        )
    except FloodWait as w:
        await asyncio.sleep(w.x)
        await bot.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"GOT FLOODWAIT OF {str(w.x)}s FROM {broadcast.chat.title}\n\n**CHANNEL ID:** `{str(broadcast.chat.id)}`",
            disable_web_page_preview=True
        )
    except Exception as e:
        await bot.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"**#ERROR_TRACEBACK:** `{e}`",
            disable_web_page_preview=True
        )
