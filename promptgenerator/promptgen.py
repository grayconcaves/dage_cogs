# prompt generator cog for Dage

# Discord
import discord
import json
import random

# Red
from redbot.core import commands, Config
from redbot.core.data_manager import bundled_data_path


class Promptgen(commands.Cog):
    """Generate a prompt."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=79797979795642, force_registration=True)
        
        kink_fp = bundled_data_path(self) / "kink.json"
        prof_fp = bundled_data_path(self) / "prof.json"
        trope_fp = bundled_data_path(self) / "trope.json"
        universe_fp = bundled_data_path(self) / "universe.json"
        
        with kink_fp.open("r") as kinks:
            self.KINKLIST = json.load(kinks)
        with prof_fp.open("r") as profs:
            self.PROFLIST = json.load(profs)
        with trope_fp.open("r") as tropes:
            self.TROPELIST = json.load(tropes)
        with universe_fp.open("r") as universe:
            self.UNIVERSELIST = json.load(universe)


    @commands.command(aliases=['prompts'])
    async def prompt(self, ctx, flag = " "):
        """Generate a romance prompt.

        To include NSFW kinks, add the 'nsfw' flag.
        e.g. `[p]prompt nsfw`

        To include Extreme NSFW prompts, add the 'extreme' flag.
        e.g. `[p]prompt extreme`
        """
        if flag != " ":
        	if flag == "extreme":
        		kink = f"Kink: {self.KINKLIST[random.randint(0,81)]}"
        	elif flag == "nsfw":
        		kink = f"Kink: {self.KINKLIST[random.randint(0,59)]}"
        	else:
        		kink = " "
        else:
        	kink = " "

        prof = self.PROFLIST[random.randint(0,137)]
        trope = self.TROPELIST[random.randint(0,21)]
        universe = self.UNIVERSELIST[random.randint(0,28)]

        msg = f"Universe: {universe} AU\nTrope: {trope}\n{kink}"

        await ctx.send(msg)

        return



        
