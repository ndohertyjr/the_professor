# import discord api
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def _reload(self, ctx, extension):
        self.bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} Cog Reloaded')


def setup(bot):
    bot.add_cog(Admin(bot))