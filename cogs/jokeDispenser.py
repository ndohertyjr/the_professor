# import discord api
import discord
from discord.ext import commands

# import random
import random

class JokeDispenser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        jokes = []
        # import jokes into list
        with open('jokes.txt', 'r') as jokeFile:
            jokes = jokeFile.readlines()

        # choose random joke
        random_choice = random.randrange(0, len(jokes))
        jokeChoice = jokes[random_choice]
        await ctx.send(jokeChoice)

def setup(bot):
    bot.add_cog(JokeDispenser(bot))