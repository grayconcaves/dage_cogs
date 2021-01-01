# Discord
import discord

# Red
from redbot.core import checks
from redbot.core import commands

BaseCog = getattr(commands, "Cog", object)

class Donate(commands.Cog):
    """Nonprofit donation for Super Dage's hosting expenses."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def donate(self, ctx):
        """Help support Super Dage's hosting expenses!"""

        thread = "If you enjoy using DaGe and would like to help with his hosting expenses, please consider donating to my ko-fi, Paypal, or Paymaya (for PH residents or account holders). \n\nYou'll be added to Super DaGe's Godparents list and get some in-bot gifts as thanks for your support!"
        donators = "\nKyu14#6421\ncarabarks#7523\nAmarok#2128\nnendo#3874\nblootooth#7872\nBetaFib#5891\nEmppu#6746\nkikibug#0435\nLady Lily Anne#8265\nsandra#3799\nfirelights56#8989\nbee (oh_fudgecakes)#3218"

        donate_details = discord.Embed(description=thread)
        donate_details.add_field(name="Check out his ko-fi here:", value="https://ko-fi.com/superdage", inline=False)
        donate_details.add_field(name="For Paypal donations: ", value="https://www.paypal.com/paypalme2/gaiandcloud", inline=False)
        donate_details.add_field(name="For Paymaya donations: ", value="https://imgur.com/a/2FMKu9h", inline=False)
        donate_details.add_field(name="For more info on donation gifts and commissions: ", value="=donategifts\n=commish")
        donate_details.set_author(name="Help support Super DaGe's hosting expenses!", url="https://ko-fi.com/post/Hello-world-Help-Donate-to-keep-Dage-alive-U7U71ROSI")
        donate_details.set_thumbnail(url="https://cdn.discordapp.com/avatars/556752532773273639/500c9b09118178e5e7fbbec7ffbd132b.png?size=1024")
        donate_details.add_field(name="Super DaGe's Godparents:", value=donators, inline=False)

        await ctx.send(embed=donate_details)

    @commands.command()
    async def donategifts(self, ctx):
        """See the gift pool for DaGe's Godparents"""

        ficgift = "As a gift for donating to Dage, you will get a free fic from me!\n\nTo see how much your donation can get you, check my commission info on **=commish**"
        await ctx.send(f"{ficgift}\n\n**All Donations will go to Super DaGe's Hosting.** I will not make profit from this bot. \nHowever, if you want to leave a tip for my work, or commission me instead, I would really appreciate it!")

    @commands.group()
    async def commission(self,ctx):
        """My commission info for fics and custom plugins."""

    @commission.command()
    async def fic(self, ctx):
        """Show info for fanfic commmissions."""

        contact = "Discord - tagape#3232     |     Twitter - galayugmagay     |     Email - gaiandcloud@gmail.com"

        fic_details = discord.Embed(description="I'm currently accepting fanfiction/writing commissions! \n\nCheck out my commission carrd here: <https://galayugmagay.carrd.co/#comms>")
        fic_details.set_author(name="Fanfiction Commission Info", url="https://galayugmagay.carrd.co/#comms")
        fic_details.set_thumbnail(url="https://cdn.discordapp.com/avatars/190114956857835520/7701beecf58a2b7029af0fa1d479469e.png?size=1024")
        fic_details.add_field(name="What I will write:", value="Fandoms I know, any pairing, prompt, or even OCs of your choice. NSFW is okay!", inline=False)
        fic_details.add_field(name="Base Rate:", value="**$3**/**₱150** per 300 words.", inline=False)
        fic_details.add_field(name="Ao3 Profiles:", value="MXTX/MDZS: <https://ao3.org/users/gracon_bacon/pseuds/weiyuanxiong>\nYuri on Ice/Other Fandoms: <https://ao3.org/users/gracon_bacon/pseuds/extra%20kanin>\n", inline=False)
        fic_details.add_field(name="Fandoms:", value="Grandmaster of Demonic Cultivation\nScum Villain's Self Saving System\nYuri!!! on Ice\nHaikyuu!!\n...and more!")
        fic_details.set_footer(text=contact)

        await ctx.send(embed=fic_details)

    @commission.command()
    async def plugin(self,ctx):
        """Show info for custom server plugins/cogs commissions."""

        contact = "Discord - tagape#3232     |     Twitter - galayugmagay     |     Email - gaiandcloud@gmail.com"

        plug_details = discord.Embed(description="I also accept paid requests for simple/basic server plugins/cogs that you can use with Dage or any other Red Bot.")
        plug_details.set_author(name="Custom Server Plugin/Cog Commission", url="https://docs.google.com/document/d/1OrGVk8HUutBdrB0zn2rZE-x8Gn13QpvThlCjcOUi9Rs/edit?usp=sharing")
        plug_details.set_thumbnail(url="https://cdn.discordapp.com/avatars/190114956857835520/7701beecf58a2b7029af0fa1d479469e.png?size=1024")
        plug_details.add_field(name="What I can make:", value="I can make basic cogs, like custom interview cogs to keep bots or members under a certain age out.", inline=False)
        plug_details.add_field(name="What I can't make:", value="Complicated commands, games, and cogs that need paid access keys. I will inform you if I believe I can fulfill your request.", inline=False)
        plug_details.add_field(name="Base Rate:", value="**$3**/**₱150** for a simple command.", inline=False)
        plug_details.set_footer(text=contact)

        await ctx.send(embed=plug_details)

