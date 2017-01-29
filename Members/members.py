import discord
from discord.ext import commands


class Members:
    """Returns number of users/bots in the server out of total members."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def users(self, ctx):
        server = ctx.message.server
        users=len([r for r in server.members if r.bot is False])
        bots=len([r for r in server.members if r.bot is True])
        if bots < 1:
            await self.bot.send_message(ctx.message.channel, "There are {} users online out of {} total members".format(users, len(server.members)))
        else:
            await self.bot.send_message(ctx.message.channel, "There are {} users and {} bots online out of {} total members".format(users, bots, len(server.members)))

def setup(bot):
    bot.add_cog(Members(bot))