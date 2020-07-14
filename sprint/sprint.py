# Sprint cog for Dage

# Discord
import discord

# Red
from redbot.core import commands, checks, Config
from redbot.core.utils.chat_formatting import pagify, humanize_timedelta

#libs
import asyncio
import time

class Sprint(commands.Cog):
    """Writing sprint cog for Dage. Perfect for servers that hold sprints!"""


    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=75092445606, force_registration=True)
        self.config.register_guild(
            defaulttimer=900,
            defaultpreptime=300,
            customtimer=0,
            custompreptime=0,
        )


    @commands.command(aliases=['sp'])
    async def sprint(self, ctx, *, timer: int):
        """Start a sprint with a timer (in minutes). Default is 30 minutes.

        e.g. `[p]sprint start 60` for a 60-minute sprint"""
        if timer == 0:
            timer = 30
        sprinttime = await self._set_time(timer)
        sprinters = await self._get_sprinters(ctx)
        mentions = [m.mention for m in sprinters]
        mention_list = mentions[-1] + ", ".join(mentions[:-1])
        start = await ctx.send("Sprint starts now! You have {} minute(s) to finish your work.".format(timer))
        await asyncio.sleep(sprinttime)
        await ctx.send("{}, the sprint has finished! Please share your word count and works on this channel.".format(mention_list))
        return


    async def _get_sprinters(self, ctx):
        """Helper function to get list of sprinters"""
        msg = await ctx.send("React to this message to join the sprint. The sprint will start in 30 seconds.")
        await msg.add_reaction('✅')
        await asyncio.sleep(30)
        msg = await ctx.channel.fetch_message(msg.id) #get the latest version of the message
        reaction = [r for r in msg.reactions if r.emoji == '\N{WHITE HEAVY CHECK MARK}'][0]
        sprinters = []
        async for user in reaction.users():
            sprinters.append(user)
        return [s for s in sprinters if not s.bot]


    async def _set_time(self, ctx):
        """Set time for sprint functions"""
        settime = ctx * 60
        return settime
    

    @commands.command(aliases=['t'])
    async def timeleft(self, ctx):
        """Check the time left for a sprint."""
        timer = self.start(timer)
        if timer > 0:
            timeleft = timer - time.time()
            return await ctx.send("You have {} left for this sprint.".format(humanize_timedelta(seconds=timeleft)))
        else:
            return await ctx.send("You are not in a sprint.")
