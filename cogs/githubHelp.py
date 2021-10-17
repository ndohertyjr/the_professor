# import discord api
import discord
from discord.ext import commands

# import random
import random
import json

class githubHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def githubHelp(self, ctx):
        with open('messages.json') as jsonMessages:
            helpMessage = json.load(jsonMessages)
        embedHelpMsg = discord.Embed(
            title=helpMessage['helpMessage'],
            description="[The Professor Discord Bot Repository](https://github.com/ndohertyjr/the_professor)")
        await ctx.send(embed=embedHelpMsg)

def setup(bot):
    bot.add_cog(githubHelp(bot))