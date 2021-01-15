# get a twitter id from a handle

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

class Twtid(commands.Cog):
    """Twtid commands"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.tweeterid = "https://tweeterid.com/ajax.php"

    
    @commands.command(aliases=['twid'])
    async def twtid(self, ctx: str) -> int:
        """Get a twitter ID from a username"""
        try:
            async with self.session.post(self.tweeterid, data={'input': handle}) as t:
                return await ctx.send(t.content.decode())
        except Exception:
            return


    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())