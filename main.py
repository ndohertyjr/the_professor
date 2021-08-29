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
GUILD_ID = os.getenv("Guild_ID")
bot = commands.Bot(command_prefix='!')

# Confirm bot is online
rules_channel = None 
rules_message_id = None
new_student_role = None

# Confirm bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} is online and connected to the server.')
    global rules_channel, rules_message_id, new_student_role
    rules_channel = discord.utils.get(bot.get_all_channels(), name='rules')
    rules_message_history = await rules_channel.history(limit = 1).flatten()
    rules_message_id = rules_message_history[0].id
    new_student_role = discord.utils.get(bot.get_guild(int (GUILD_ID)).roles, name="New Student")


# ****MAIN CODE BODY GOES BELOW HERE****

# Bot Initial Rules Agreement

@bot.event
async def on_raw_reaction_add(payload):

    if (payload.message_id != rules_message_id):
        return
    
    if (payload.emoji.name == '👍'):
        print(payload.member.name + " accepted the rules")
        await payload.member.add_roles(new_student_role, reason=None, atomic=True)
    elif (payload.emoji.name == '👎'):
        print(payload.member.name + " declined the rules")
    else:
        print("Invalid Option")

        
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

