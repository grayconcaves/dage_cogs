# Sprint cog for Dage

# Discord
import discord

# Red
from redbot.core import commands, checks, Config
from redbot.core.utils.chat_formatting import pagify

#libs
import asyncio
import time

BaseCog = getattr(commands, "Cog", object)


class Sprint(BaseCog):
    """Writing sprint cog for Dage. Perfect for servers that hold sprints!"""


    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['sp'])
    async def sprint(self, ctx):
        """Group commands for sprint settings"""
        pass


    async def _get_sprinters(self, ctx):
        """Helper function to get list of sprinters"""
        msg = await ctx.send("React to this message to join the sprint. The sprint will start in 30 seconds.")
        await msg.add_reaction('✅')
        time.sleep(30)
        msg = await ctx.channel.fetch_message(msg.id) #get the latest version of the message
        reaction = [r for r in msg.reactions if r.emoji == '\N{WHITE HEAVY CHECK MARK}'][0]
        sprinters = []
        async for user in reaction.users():
            sprinters.append(user)
        return [s for s in sprinters if not s.bot]


    @staticmethod
    def _get_name_string(ctx, uid: int, domention: bool):
        """Returns a member identification string from an id, checking for exceptions."""
        member = ctx.guild.get_member(uid)
        if member:
            return member.mention if domention else member.display_name
        return _('<removed member {uid}>').format(uid=uid)


    @sprint.command()
    async def start(self, ctx, timer: int):
        """Start a sprint with a timer (in minutes)

        e.g. `=sprint start 30` for a 30-minute sprint"""
        sprinttime = 60 * timer
        sprinters = await self._get_sprinters(ctx)
        mentions = [m.mention for m in sprinters]
        mention_list = mentions[-1] + ", " + ", ".join(mentions[:-1])
        if len(sprinters) <= 1:
            return await ctx.send("You need at least 2 members to start the sprint.")
        start = await ctx.send("Sprint starts now! You have {} minute(s) to finish your work.".format(timer))
        time.sleep(sprinttime)
        await ctx.send("{}, the sprint has finished! Please share your word count and works on this channel.".format(mention_list))