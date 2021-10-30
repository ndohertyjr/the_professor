'''
Test commands for the SQL DB
Commands should not be included in production environment
'''

# import discord api
from  discord.ext import commands

# import methods
from controllers.userTable import *
from controllers.jokesTable import *

class SQLTesting(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ''' *** USER TABLE COMMANDS ***'''
    # Add users
    @commands.command()
    async def testadd(self, ctx):
        add_user(1111, "thegunnersdream", "admin", 0)
        add_user(2222, "test", "admin", 0)
        add_user(3333, "banana man", "admin", 0)
        add_user(1111, "thegunnersdream", "admin", 0)
        add_user(4444, "buddy", "tester", 100)
        add_user(5555, "butthead", "dude", 69)
        add_user(6666, "beavis", "other dude", 420)

    # Find one user by username
    @commands.command()
    async def testfind(self, ctx):
        get_user_id("thegunnersdream")

    # Find all users
    @commands.command()
    async def testfindall(self, ctx):
        print(get_all_usernames())

    # Find one user by ID
    @commands.command()
    async def testfindone(self, ctx):
        print(get_username(3333))

    # Find user role by ID
    @commands.command()
    async def testfindrole(self, ctx):
        print(get_user_role(4444))

    # Find user's points by ID
    @commands.command()
    async def testfindpoints(self, ctx):
        print(get_user_points(5555))

    # Update points by ID
    @commands.command()
    async def testupdatepoints(self, ctx):
        print(get_user_points(2222), "Old points")
        update_user_points(2222, -25)
        print(get_user_points(2222), "New points")

    # Update specific username by id
    @commands.command()
    async def testupdateuser(self, ctx):
        update_user_name(2222, "Captain Insaino")

    # Update user role by ID
    @commands.command()
    async def testupdaterole(self, ctx):
        update_user_role(3333, "Master and Commander of the Far Side of the Sea")

    # Delete all users
    @commands.command()
    async def testdeleteall(self, ctx):
        for i in get_all_usernames():
            user = get_user_id(i)
            delete_user(user)
        print("Done!")

    ''' *** JOKES TABLE COMMANDS *** '''

    # Get all jokes
    @commands.command()
    async def testgetalljokes(self, ctx):
        print(get_all_jokes())

    # Get random joke
    @commands.command()
    async def testgetrandomjoke(self, ctx):
        print(get_random_joke())

    # Update joke by ID
    @commands.command()
    async def testupdatejoke(self, ctx):
        update_one_joke(18, "What do you call a pig that does karate?  A pork chop!")

    # Delete joke by ID
    @commands.command()
    async def testdeletejoke(self, ctx):
        delete_joke(18)


def setup(bot):
    bot.add_cog(SQLTesting(bot))
