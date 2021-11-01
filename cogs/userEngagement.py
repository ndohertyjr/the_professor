"""
System to track member engagement and update roles based on amount and frequency of engagement
"""

# Import controllers
from controllers.rolesTable import *
from controllers.userTable import *
import asyncio

# Import discord libraries
from discord.ext import commands


# Bot initialization to sync with current server data
class UserEngagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # evaluate and update points on message sent
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            increment_points(message.author.id)


def setup(bot):
    bot.add_cog(UserEngagement(bot))
