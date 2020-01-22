# Discord
import discord

# Red
from redbot.core import commands

BaseCog = getattr(commands, "Cog", object)

class Howto(commands.Cog):
    """Easy-to-use FAQ for DaGe via Google Slides"""

    def __init__(self, bot):
    	self.bot = bot

    @commands.command()
    async def howto(self, ctx):
    	"""See DaGe's How to"""

    	thread = "Having trouble using DaGe? \n\nConfused by `>>help`? \n\nDon't worry, 'How to Use DaGe' is here!"
 
    	faq = discord.Embed(description=thread)
    	faq.add_field(name="Check it out on Google Slides:", value="https://bit.ly/2YMpFiW")
    	faq.set_author(name="DaGe's Visual Guide", url="https://docs.google.com/presentation/d/e/2PACX-1vSXfWU2q478KEJEcUu4eDYVTZJ3UbYupkw8Ywgk3LJbaYL2mQSeYEXeHFrY79w0Yr8F_vo7tBck_Nmc/pub?start=false&loop=false&delayms=3000")
    	faq.set_thumbnail(url="https://cdn.discordapp.com/avatars/556752532773273639/500c9b09118178e5e7fbbec7ffbd132b.png?size=1024")

    	await ctx.send(embed=faq)
