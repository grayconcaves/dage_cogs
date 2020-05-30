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

        thread = "Having trouble using DaGe? \n\nConfused by `>>help`? \n\nDon't worry, 'DaGe's Docs' is here!"
        
        faq = discord.Embed(description=thread)
        faq.add_field(name="Check it out on Google Docs:", value="https://bit.ly/dagesdocs")
        faq.add_field(name="Annie (annie#9358) made a better Adventure guide for new adventurers here!", value="http://bit.ly/2W3atiS")
        faq.set_author(name="DaGe's Doc's", url="https://bit.ly/dagesdocs")
        faq.set_thumbnail(url="https://cdn.discordapp.com/avatars/556752532773273639/500c9b09118178e5e7fbbec7ffbd132b.png?size=1024")

        await ctx.send(embed=faq)
        return
