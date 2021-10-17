# import discord api
import discord
from discord.ext import commands

# imports for token
from dotenv import load_dotenv
import json
import os
from cogs.greeting import Greeting
from cogs.jokeDispenser import JokeDispenser


# Server imports
#from server import keep_online

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
bot.add_cog(Greeting(bot))


#Joke dispenser
bot.add_cog(JokeDispenser(bot))

# Github help command
@bot.command()
async def githubHelp(ctx):
    with open('messages.json') as jsonMessages:
        helpMessage = json.load(jsonMessages)
    embedHelpMsg = discord.Embed(
        title=helpMessage['helpMessage'],
        description="[The Professor Discord Bot Repository](https://github.com/ndohertyjr/the_professor)")
    await ctx.send(embed=embedHelpMsg)


# ****MAIN CODE BODY GOES ABOVE HERE****

# Keep thread open on the server
#keep_online()

# Run bot
bot.run(TOKEN)

