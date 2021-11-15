'''
Test commands for the Mongo DB
Commands should not be included in production environment
'''

# import discord api
from discord.ext import commands

#import methods
from controllers.userController import *
from controllers.rolesController import *


class MongoTesting(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    '''MONGO USER TABLE COMMANDS'''
    #Add users
    @commands.command()
    async def testAddMongo(self, ctx):
        add_user_mongo(1234, "neil", 1000)
        add_user_mongo(1567, "joe", 101)
        add_user_mongo(1234, "jim", 10)
        add_user_mongo(1000000, "bethany", -1)
        add_user_mongo(-1, "taylor", 100)

    # Find one user by username
    @commands.command()
    async def testFindIDMongo(self, ctx):
        print(get_user_id("neil"))

    # Find one user by username
    @commands.command()
    async def testFindNameMongo(self, ctx):
        print(get_username(1234))

    # Find all users
    @commands.command()
    async def testFindAllMongo(self, ctx):
        print(get_all_usernames())

    # Find user points
    @commands.command()
    async def testGetUserPointsMongo(self, ctx):
        print(get_user_points(1567))

    # Find user roles
    @commands.command()
    async def testGetUserRolesMongo(self, ctx):
        print(get_user_roles(1234))
        print(get_user_roles(1567))

    # Update username
    @commands.command()
    async def testUpdateNameMongo(self, ctx):
        update_user_name(1000000, "Banana Man")

    # Update user points
    @commands.command()
    async def testUpdatePointsMongo(self, ctx):
        update_user_points(1000000, 420)

    # Add new role to user
    @commands.command()
    async def testAddUserRoleMongo(self, ctx):
        add_new_user_role(1234, 69420, "God Emperor of Man")
        add_new_user_role(1234, 90000, "Vegeta")

    # Delete user
    @commands.command()
    async def testDeleteUserMongo(self, ctx):
        delete_user(1234)

    # Delete user
    @commands.command()
    async def testDeleteUserRoleMongo(self, ctx):
        delete_user_role(1234, 69420)


    ''' *** ROLE TABLE COMMANDS *** '''


    # Add role by ID
    @commands.command()
    async def testAddRoleMongo(self, ctx):
        add_role(1234, "First", 10)
        add_role(2345, "Second", 25)
        add_role(3456, "Third", 50)

    # Find role by ID
    @commands.command()
    async def testFindRoleNameMongo(self, ctx):
        print(get_role_name(1234))

    # Find role by name
    @commands.command()
    async def testFindRoleIdMongo(self, ctx):
        print(get_role_id("Second"))

    # Find all roles
    @commands.command()
    async def testFindAllRolesMongo(self, ctx):
        print(get_all_roles())

    # Find all roles
    @commands.command()
    async def testFindMaxPtsMongo(self, ctx):
        get_role_max_pts(2345)

    # Update role by ID
    @commands.command()
    async def testUpdateRoleMongo(self, ctx):
        update_role(3456, "Test 2")

    #Update max pts by ID
    @commands.command()
    async def testUpdateMaxPtsMongo(self, ctx):
        update_max_pts(1234, 500)

    # Delete role by ID
    @commands.command()
    async def testDeleteRoleMongo(self, ctx):
        delete_role(3456)


def setup(bot):
    bot.add_cog(MongoTesting(bot))



