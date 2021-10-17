# import discord api
import discord
from discord.ext import commands
from main import GUILD_ID
from main import RULES_MESSAGE_ID

class RulesAgreement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rules_message_id = None
        self.new_student_role = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.rules_message_id = RULES_MESSAGE_ID
        self.new_student_role = discord.utils.get(self.bot.get_guild(int (GUILD_ID)).roles, name="New Student")
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if (str(payload.message_id) != self.rules_message_id):
            print(type(payload.message_id))
            print(payload.message_id)
            print(type(self.rules_message_id))
            print(self.rules_message_id)
            return
        
        if (payload.emoji.name == '👍'):
            print(payload.member.name + " accepted the rules")
            await payload.member.add_roles(self.new_student_role, reason=None, atomic=True)
        elif (payload.emoji.name == '👎'):
            print(payload.member.name + " declined the rules")
        else:
            print("Invalid Option")

def setup(bot):
    bot.add_cog(RulesAgreement(bot))
 