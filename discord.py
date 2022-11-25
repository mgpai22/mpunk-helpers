from discord_webhook import DiscordWebhook, DiscordEmbed
import os
from dotenv import load_dotenv
import os
load_dotenv()

webhookLink = os.getenv("WEBHOOK")
webhook = DiscordWebhook(url=webhookLink)


# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color='03b2f8') number

def discordCall(position, score):  # sends discord message of the NFT that has been sent
    embed = DiscordEmbed(title='Mpunk Status Update', description=f'Line position is {position} \n \n Score is {score}', color='03b2f8')
    # add embed object to webhook
    webhook.add_embed(embed)
    response = webhook.execute()
