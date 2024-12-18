from pyrogram import Client
import pyromod.listen
from Config import Var
from os import getcwd

StreamBot = Client(
    name='Web Streamer',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workdir="Vortex",
    plugins={"root": "Vortex/bot/plugins"},
    workers=5
)

multi_clients = {}
work_loads = {}
