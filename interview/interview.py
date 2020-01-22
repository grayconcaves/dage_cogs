# interview cog from v2 to v3

# Discord
import discord

# Red
from redbot.core import Config
from redbot.core import checks
from redbot.core import commands
from redbot.core.utils.predicates import MessagePredicate

#libs
import asyncio
import time

BaseCog = getattr(commands, "Cog", object)


class Interview(commands.Cog):
    """Interview cog for We're Old and Tired server only. Needs a gatekeeping role."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=9811198108111121, force_registration=True)
        default_global = {}
        default_guild = {"announce": None, "roles": {}}

    @commands.command()
    async def interview(self, ctx):
        """Starts the interview."""
        guild = ctx.guild
        gate = discord.utils.get(guild.roles, id=571025813688942603)
        #This is the gate role.
        role = discord.utils.get(guild.roles, id=593082985750986763)
        #This is the role people want to get into.

        await ctx.send("**Thank you for joining our server!** \n\nWe'd like to ask three questions before you can fully join our chat. Please answer each question truthfully within 30 seconds.", delete_after=30)
        time.sleep(10)

        await ctx.send("__Question #1: How old are you?__ \n(Number only please, e.g. **12**, **31**)", delete_after=30)
        age = MessagePredicate.valid_int(ctx)
        try:
            await self.bot.wait_for("message", check=age, timeout=30)
        except:
            age=0
            ctx.send("Interview timed out.", delete_after=10)
            return

        if age.result < 100:
            if age.result < 25:
                await ctx.send("Sorry. This server is for people aged 25+ only. \n\nIf you made a mistake, please restart the interview.", delete_after=10)
                return
        else:
            await ctx.send("You can't be more than 100 years old. Please stop messing with me.", delete_after=10)
            return

        await ctx.send("Thank you! \n\n__Question #2: Are you a student or are you already working?__", delete_after=30)
        status = MessagePredicate.same_context(user=ctx.author)
        try:
            await self.bot.wait_for("message", check=status, timeout=30)
        except:
            await ctx.send("Interview timed out.", delete_after=10)
            return

        await ctx.send("Thank you! \n\nNow, on to the most important question: \n__Do your knees crack?__", delete_after=30)
        crack = MessagePredicate.same_context(user=ctx.author)
        try:
            await self.bot.wait_for("message", check=crack, timeout=30)
        except:
            ctx.send("Interview timed out.", delete_after=10)
            return

        await ctx.send(":tada: Congratulations {}!:tada: \n\nYou may now enter the rest of the server. Welcome to the chat!".format(ctx.author.mention))
        await ctx.author.add_roles(role, reason="Entry allowed")
        await ctx.author.remove_roles(gate, reason="Entry already granted, no need for gate")

