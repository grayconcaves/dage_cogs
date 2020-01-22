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
        donators = "\nKyu14#6421\ncarabarks#7523\nAmarok#2128\nnendo#3874\nblootooth#7872\nBetaFib#5891\nEmppu#6746\nkikibug#0435\nLady Lily Anne#8265"

        donate_details = discord.Embed(description=thread)
        donate_details.add_field(name="Check out the ko-fi post here:", value="https://ko-fi.com/Blog/Post/Super-DaGe-Hosting-Expenses-[Call-for-DonationsCo-Z8Z8YBCT", inline=False)
        donate_details.add_field(name="For Paypal donations: ", value="https://www.paypal.com/paypalme2/gaiandcloud", inline=False)
        donate_details.add_field(name="For Paymaya donations: ", value="https://imgur.com/a/2FMKu9h", inline=False)
        donate_details.add_field(name="For more info on donation gifts and commissions: ", value="=donategifts\n=commish")
        donate_details.set_author(name="Help support Super DaGe's hosting expenses!", url="https://ko-fi.com/Blog/Post/Super-DaGe-Hosting-Expenses-[Open-Call-for-Donatio-K3K7YB25")
        donate_details.set_thumbnail(url="https://cdn.discordapp.com/avatars/556752532773273639/500c9b09118178e5e7fbbec7ffbd132b.png?size=1024")
        donate_details.add_field(name="Super DaGe's Godparents:", value=donators, inline=False)

        await ctx.send(embed=donate_details)

    @commands.command()
    async def donategifts(self, ctx):
        """See the gift pool for DaGe's Godparents"""

        gift1 = "**:star: 1 Legendary Chest** (5 for 4 ko-fi) - __1 ko-fi / $3 / ₱150__ :star:\n\n"
        gift2 = "**:star: 1 Random high-stat Legendary Item** - __4 ko-fi / $12 / ₱500__ :star:\n- Choose one stat that will have a value of 10 or above.\n\n"
        gift3 = "**:star: 1 Custom Ranger Pet** - __6 ko-fi / $18 / ₱750__ :star:\n- Name your own pet! You can choose its diplomacy requirement (since it will be automatically added to the pet pool) but its bonus will be a random number from 1.75 to 2.5.\n- You can replace your current pet with your custom pet. If you change classes then return to ranger, I will give you back your custom pet.\n\n"
        gift4 = "**:star: 1 Custom Legendary Item** - __16 ko-fi / $48 / ₱2100__ :star:\n- Name your own Legendary item! It will have 1 random high (10-14) stat of your choice, and you can also choose its item slot. The rest of its stats will be random from -3 to 7.\n- To get a second high stat, just add __4 ko-fi__ and your item will be updated.\n- Your custom item will not be added to the chest pool. It will be added to your account only. To get a second copy of your item to give or trade away to a friend, just add __4 ko-fi__.\n- If you *accidentally* sell your custom item, I will give it back to you.\n\n"
        ficgift = "If you want a more tangible gift, I can also gift you a fic!\n :star:**300-500-word Fanfic Gift** - __1 ko-fi / $3 / ₱150__ :star:\n- See my commission info on **=commish**\n\n"
        await ctx.send("If you are interested in donating for DaGe's hosting expenses, here are some gifts to sweeten the pot for you: \n\n{}{}{}{}{}**All Donations will go to Super DaGe's Hosting.** I will not make profit from this bot. However, if you want to leave a tip for my work, or commission me instead, I would really appreciate it!".format(gift1, gift2, gift3, gift4, ficgift))

    @commands.group()
    async def commission(self,ctx):
        """My commission info for fics and custom plugins."""

    @commission.command()
    async def fic(self, ctx):
        """Show info for fanfic commmissions."""

        contact = "Discord - tagape#3232     |     Twitter - galayugmagay     |     Email - gaiandcloud@gmail.com"

        fic_details = discord.Embed(description="I'm currently accepting fanfiction/writing commissions! \n\nCheck out my commission card here: <https://docs.google.com/document/d/1OrGVk8HUutBdrB0zn2rZE-x8Gn13QpvThlCjcOUi9Rs/edit?usp=sharing>")
        fic_details.set_author(name="Fanfiction Commission Info", url="https://docs.google.com/document/d/1OrGVk8HUutBdrB0zn2rZE-x8Gn13QpvThlCjcOUi9Rs/edit?usp=sharing")
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
        plug_details.add_field(name="Plugins/cogs I made:", value="**ao3**\n**howto**\n**donate**\n**interview** (for one server)", inline=False)
        plug_details.set_footer(text=contact)

        await ctx.send(embed=plug_details)

