# import discord api
import discord
from discord.ext import commands
# imports for token
from dotenv import load_dotenv
import os

# load token
load_dotenv('.env')
TOKEN = os.getenv("TOKEN")
bot = commands.Bot(command_prefix='!')

# Confirm bot is online
rules_channel = None 
rules_message_id = None
test_role = None

@bot.event
async def on_ready():
    print(f'{bot.user} is online and connected to the server.')
    global rules_channel, rules_message_id, test_role
    rules_channel = await discord.utils.get(bot.get_all_channels(), name='rules')
    rules_message_history = await rules_channel.history(limit = 1).flatten()
    rules_message_id = rules_message_history[0].id
    test_role = await discord.utils.get(bot.get_guild(860919967749505025).roles, name="TestRole")

# ****MAIN CODE BODY GOES BELOW HERE****

# Bot Initial Rules Agreement

@bot.event
async def on_raw_reaction_add(payload):

    if (payload.message_id != rules_message_id):
        return
    
    if (payload.emoji.name == '👍'):
        print(payload.member.name + " accepted the rules")
        await payload.member.add_roles(test_role, reason=None, atomic=True)
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
