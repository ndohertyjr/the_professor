# import discord api
from discord.ext import commands
from discord import Client, guild
import discord

# imports for token
from dotenv import load_dotenv
import os


# Server imports
from server import keep_online
from controllers.jokesTable import *
from controllers.userTable import *
from model.database import *

# load token
load_dotenv('.env')
TOKEN = os.getenv("TOKEN")
GUILD_ID = os.getenv("Guild_ID")
RULES_MESSAGE_ID = os.getenv("RulesMessageId")
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


# Confirm bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} is online and connected to the server.')
    # Establish DB and tables
    create_connection()
    create_user_table()
    create_jokes_table()
    create_roles_table()
    add_jokes()


''' 
****MAIN CODE BODY GOES BELOW HERE**** 
'''

# Admin
bot.load_extension('cogs.admin')

# Bot Initial Rules Agreement
bot.load_extension('cogs.rulesagreement')

# Bot greeting test feature
bot.load_extension('cogs.greeting')

# Joke dispenser
bot.load_extension('cogs.jokeDispenser')

# Github help command
bot.load_extension('cogs.githubHelp')

# SQL DB testing commands
bot.load_extension('cogs.sqlTesting')


# ****MAIN CODE BODY GOES ABOVE HERE****
#FIXME
# Keep thread open on the server
keep_online()



# Run bot
bot.run(TOKEN)

