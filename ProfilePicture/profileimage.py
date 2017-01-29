import discord
from discord.ext import commands
from random import choice, randint


class EmbedProfileImg:
    """Returns the selected users profile picture in an embedded message."""


    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def embedprofileimgae(self, ctx, user: discord.Member=None):
        author = ctx.message.author
        em = discord.Embed(colour=author.colour)
        if not user:
            user = author
        if user.avatar_url:
            em.set_image(url=user.avatar_url)
        else:
            em.set_image(url=user.default_avatar_url)
        await self.bot.say(emptyrand, embed=em)
def setup(bot):
    bot.add_cog(EmbedProfileImg(bot))