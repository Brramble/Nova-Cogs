import discord
from discord.ext import commands

class Intro:
    """Introduction"""
    
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def intro(self, ctx):
        """View my Infomation!"""

        user = ctx.message.author
        author = user
        
        em = discord.Embed(description='Bot Description.', colour=user.colour)
        em.set_author(name='Title!' icon_url='IMAGE URL')
        em.add_field(name='FieldName', value='Description')
        em.add_field(name='FieldName', value='Description')
        em.set_footer(text='Description')
        await self.bot.say(embed=em)

def setup(bot):
    n = Intro(bot)
    bot.add_cog(n)