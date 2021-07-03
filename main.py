# import discord api
import discord
# imports for token
from dotenv import load_dotenv
import os
# import to keep server running
from keep_online import keep_online

# load token
load_dotenv('.env')
TOKEN = os.getenv("TOKEN")
client = discord.Client()

# Confirm bot is online
@client.event
async def on_ready():
    print(f'{client.user} is online and connected to the server.')


# ****MAIN CODE BODY GOES BELOW HERE****


# Bot greeting test feature
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Hello'):
        channel = message.channel
        await channel.send('I AM ALIVE')


# ****MAIN CODE BODY GOES ABOVE HERE****


# Respond to pings to keep server running using uptimerobot.com
keep_online()

# Connect to the server
client.run(TOKEN)
