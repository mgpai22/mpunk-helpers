import discord_notify as dn
from dotenv import load_dotenv
import os
load_dotenv()

def discordCall(position, score):
    obj = dn.Notifier(os.getenv("WEBHOOK"))
    obj.send(f"``` Mpunk Status Update \n \n Line position is: {position} \n \n Score is: {score}```", print_message=False)

