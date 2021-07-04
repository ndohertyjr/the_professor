# import discord api
import discord
from discord import emoji
from discord.ext import commands
# imports for token
from dotenv import load_dotenv
import os

# load token
load_dotenv('.env')
TOKEN = os.getenv("TOKEN")
bot = commands.Bot(command_prefix='!')

# Confirm bot is online


@bot.event
async def on_ready():
    print(f'{bot.user} is online and connected to the server.')

# ****MAIN CODE BODY GOES BELOW HERE****

# Bot Initial Rules Agreement
rules_message_id = 860962384276226078
@bot.event
async def on_raw_reaction_add(payload):
    print(payload)

    if (payload.message_id != rules_message_id):
        return
    
    if (payload.emoji.name == '👍'):
        print(payload.member.name + " accepted the rules")
    elif (payload.emoji.name == '👎'):
        print(payload.member.name + " declined the rules")
    else:
        print("Invalid Option")


# Bot greeting test feature

@bot.command()
async def hello(ctx):
    await ctx.send('I AM ALIVE')

# ****MAIN CODE BODY GOES ABOVE HERE****

# Connect to the server
bot.run(TOKEN)
