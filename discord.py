from discord_webhook import DiscordWebhook, DiscordEmbed
import os
import re

webhookLink = "https://discord.com/api/webhooks/1045574498763669504/xxqx9wuT6SCF3cy6tUoAQdckzHjrkHi_C_Fy8xDOZrQ4GKEjFA5npZHzu6lGZNzhPQt7"
webhook = DiscordWebhook(url=webhookLink)


# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color='03b2f8') number

def discordCall(position, score):  # sends discord message of the NFT that has been sent
    embed = DiscordEmbed(title='Mpunk Status Update', description=f'Line position is {position} \n \n Score is {score}', color='03b2f8')
    # add embed object to webhook
    webhook.add_embed(embed)
    response = webhook.execute()
