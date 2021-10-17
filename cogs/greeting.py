# import discord api
import discord
from discord.ext import commands

class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('I AM ALIVE')

def setup(bot):
    bot.add_cog(Greeting(bot))
    