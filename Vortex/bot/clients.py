import asyncio
import logging
from Config import Var
from Config import *
from pyrogram import Client
from . import multi_clients, work_loads, StreamBot

async def initialize_clients():
    if Var.MULTI_CLIENT:
        all_tokens={1:Var.MULTI_TOKEN1,2:Var.MULTI_TOKEN2,3:Var.MULTI_TOKEN3,4:Var.MULTI_TOKEN4,5:Var.MULTI_TOKEN5,6:Var.MULTI_TOKEN6,7:Var.MULTI_TOKEN7,8:Var.MULTI_TOKEN8,9:Var.MULTI_TOKEN9,10:Var.MULTI_TOKEN10}
        if not any(all_tokens.values()):
            multi_clients[0]=StreamBot
            work_loads[0]=0
            print("No additional clients found, using default client")
            return
    else:
        multi_clients[0]=StreamBot
        work_loads[0]=0
        print("Multi-client is off, continuing with default client")

    async def start_client(client_id, token):
        try:
            print(f"Starting - Client {client_id}")
            if client_id == len(all_tokens):
                await asyncio.sleep(2)
                print("This will take some time, please wait...")
            client = await Client(
                name=str(client_id),
                api_id=Var.API_ID,
                api_hash=Var.API_HASH,
                bot_token=token,
                sleep_threshold=Var.SLEEP_THRESHOLD,
                no_updates=True,
                in_memory=True
            ).start()
            work_loads[client_id] = 0
            return client_id, client
        except Exception:
            logging.error(f"Failed starting Client - {client_id} Error:", exc_info=True)
    
    clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items()])
    multi_clients.update(dict(clients))
    if len(multi_clients) != 1:
        Var.MULTI_CLIENT = True
        print("Multi-Client Mode Enabled")
    else:
        print("No additional clients were initialized, using default client")
