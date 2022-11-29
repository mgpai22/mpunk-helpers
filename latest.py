import time

import requests
from dotenv import load_dotenv
import os

from discord import discord_call_latest, discord_successful_mint
from mint import mint

load_dotenv()

my_wallet = os.getenv("ADDRESS")
# my_wallet = "0x76F89FE4A717eB1902B701549AF8D1e1A4067bae"

while True:
    try:
        res = requests.get("https://mpunkspool.com/latest.txt").json()
        latest_address = res['address']
        success = res['success']
        if latest_address == my_wallet and success is True:
            print("found")
            discord_call_latest()
            try:
                print("trying to mint")
                txid = mint()
                discord_successful_mint(txid)
            except Exception as e:
                print("mint failed")
                pass
        time.sleep(30)
    except Exception as e:
        time.sleep(30)
        pass
