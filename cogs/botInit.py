"""
Methods to be run on initialization of the bot to the server
"""
from discord import Guild, Client

from model.sqlModel import *
from model.mongoModel import *
from controllers.userController import *
from controllers.userTable import *
from controllers.jokesTable import *
from controllers.rolesTable import *
from discord.ext import commands
from discord import Role
from main import GUILD_ID


# Populate roles database from current server roles
def populate_roles_database(bot):
#FIXME CHANGE IT MONGO YOU DUMB SHIT
    for guild in bot.guilds:
        if str(guild.id) == GUILD_ID:
            for role in guild.roles:
                add_role(role.id, role.name)


# Populate users SQL database from current server members
def populate_user_database_SQL(bot):
    for member in bot.get_all_members():
        for all_roles in member.roles:
            current_role_name = all_roles.name

        add_user(member.id, member.name, current_role_name, 0)


# Populate users Mongo DB from current server members
def populate_user_database_Mongo(bot):
    for member in bot.get_all_members():
        add_user_mongo(member.id, member.name, 0)


def assign_member_roles(bot):
    for guild in bot.guilds:
        if str(guild.id) == GUILD_ID:
            for role in guild.roles:
                pass


# Bot initialization to sync with current server data
class BotInit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        # FIXME Remove SQL
        # create_connection()
        # create_roles_table()
        # create_jokes_table()
        # create_user_table()

        populate_user_database_Mongo(self.bot)

        #FIXME Populate Roles
        #populate_roles_database(self.bot)
        #populate_user_database(self.bot)
        add_jokes()


def setup(bot):
    bot.add_cog(BotInit(bot))
