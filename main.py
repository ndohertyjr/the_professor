# import discord api
import discord
from discord.ext import commands
# import random
import random
# imports for token
from dotenv import load_dotenv
import os


# Server imports
from server import keep_online

# load token
load_dotenv('.env')
TOKEN = os.getenv("TOKEN")
bot = commands.Bot(command_prefix='!')



# Confirm bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} is online and connected to the server.')


# ****MAIN CODE BODY GOES BELOW HERE****


# Bot greeting test feature
@bot.command()
async def hello(ctx):
    await ctx.send('I AM ALIVE')


#Joke dispenser
@bot.command()
async def joke(ctx):
    jokes = []
    # import jokes into list
    with open('jokes.txt', 'r') as jokeFile:
        jokes = jokeFile.readlines()

    # choose random joke
    random_choice = random.randrange(0, len(jokes))
    jokeChoice = jokes[random_choice]
    await ctx.send(jokeChoice)


# ****MAIN CODE BODY GOES ABOVE HERE****

# Keep thread open on the server
keep_online()

# Run bot
bot.run(TOKEN)

