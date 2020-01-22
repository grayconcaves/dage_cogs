# get a random shiba inu pic

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

class Shibe(commands.Cog):
    """Get you a Shibe!"""

     def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.shibapi = "http://shibe.online/api/shibes?count=1"

    
    @commands.command()
    async def shibe(self, ctx):
        """Get a random shiba inu picture"""
        try:
            async with self.session.get(self.shibapi) as s:
                shibe = await s.json()
            await ctx.send(shibe[0])
        except:
            return


    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())
