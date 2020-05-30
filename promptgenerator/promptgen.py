# prompt generator cog for Dage

# Discord
import discord
import json
import random

# Red
from redbot.core import commands, Config
from redbot.core.data_manager import bundled_data_path
from redbot.core.utils.chat_formatting import humanize_list


class Promptgen(commands.Cog):
    """Generate a prompt."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=79797979795642, force_registration=True)
        
        kink_fp = bundled_data_path(self) / "kink.json"
        extremekink_fp = bundled_data_path(self) / "extremekink.json"
        prof_fp = bundled_data_path(self) / "prof.json"
        nsfwprof_fp = bundled_data_path(self) / "nsfwprof.json"
        trope_fp = bundled_data_path(self) / "trope.json"
        nsfwtrope_fp = bundled_data_path(self) / "nsfwtrope.json"
        universe_fp = bundled_data_path(self) / "universe.json"
        
        with kink_fp.open("r") as kinks:
            self.KINKLIST = json.load(kinks)
        with extremekink_fp.open("r") as ekinks:
            self.EXTREMEKINKLIST = json.load(ekinks)
        with prof_fp.open("r") as profs:
            self.PROFLIST = json.load(profs)
        with nsfwprof_fp.open("r") as nsfwprofs:
            self.NSFWPROFLIST = json.load(nsfwprofs)
        with trope_fp.open("r") as tropes:
            self.TROPELIST = json.load(tropes)
        with nsfwtrope_fp.open("r") as nsfwtropes:
            self.NSFWTROPELIST = json.load(nsfwtropes)
        with universe_fp.open("r") as universe:
            self.UNIVERSELIST = json.load(universe)


    @commands.command(aliases=['prompts'])
    async def prompt(self, ctx, numtropes=1):
        """Generate a romance prompt.

        To specify the number of tropes (challenges), just include a number. MAX: 5
        e.g. `[p]prompt 2`
        """

        # DATA VALIDATION
        if numtropes < 0 or numtropes > 5:
            return await ctx.send("Please use a number from 0-5.")

        # CODE PROPER
        prof = f"{str(random.choice(self.PROFLIST))}"
        trope = f"Challenge: {humanize_list(random.sample(self.TROPELIST, k=numtropes))}"
        universe = f"Universe: **{str(random.choice(self.UNIVERSELIST))} AU**"

        msg = f"{universe}\n{trope}\nBonus: One of the characters is {prof}."

        await ctx.send(msg)

        return

    @commands.command(aliases=['smutprompts'])
    @commands.is_nsfw()
    async def smutprompt(self, ctx, numtropes=1, numkinks=1, flag=" "):
        """Generate a smutty romance prompt.

        To specify the number of tropes (challenges), just include a number. MAX: 5
        e.g. `[p]smutprompt 2`

        To include Extreme NSFW kinks, add the 'extreme' flag.
        e.g. `[p]smutprompt 2 extreme `

        To specify the number of kinks, just include a number AFTER the number of tropes. MAX: 5
        e.g. `[p]smutprompt 2 2 extreme ` or `[p]smutprompt 2 2`
        """

        # DATA VALIDATION
        if numtropes < 0 or numtropes > 5:
            return await ctx.send("Please use a number from 0-5.")
        if numkinks < 0 or numkinks > 5:
            return await ctx.send("Please use a number from 0-5.")

        # CODE PROPER
        if flag == "extreme":
            kink = f"Kink: {humanize_list(random.sample((self.EXTREMEKINKLIST+self.KINKLIST), k=numkinks))}\n"
            prof = f"{str(random.choice(self.NSFWPROFLIST))}"
            trope = f"Challenge: {humanize_list(random.sample(self.NSFWTROPELIST, k=numtropes))}"
        else:
            kink = f"Kink: {humanize_list(random.sample(self.KINKLIST, k=numkinks))}\n"
            prof = f"{str(random.choice(self.NSFWPROFLIST))}"
            trope = f"Challenge: {humanize_list(random.sample(self.NSFWTROPELIST, k=numtropes))}"
        
        universe = f"Universe: **{str(random.choice(self.UNIVERSELIST))} AU**"

        msg = f"{universe}\n{trope}\n{kink}\nBonus: One of the characters is {prof}."

        await ctx.send(msg)

        return


    @commands.command(aliases=['kink'])
    @commands.is_nsfw()
    async def kinks(self, ctx, numkinks=1):
        """Generates a list of kinks.

        To generate a list of kinks:
        ```
        [p]kinks <number up to 6>
        """

        # DATA VALIDATION
        if numkinks < 1 or numkinks > 6:
            return await ctx.send("Please use a number from 1 to 6.")

        kink = random.sample(self.KINKLIST, k=numkinks)

        await ctx.send(', '.join(kink))

        return

    @commands.command(aliases=['extremekink'])
    @commands.is_nsfw()
    async def extremekinks(self, ctx, numkinks=1):
        """Generates a list of nsfw + extreme kinks.

        To generate a list of nsfw + extreme kinks:
        ```
        [p]extremekinks <number up to 6>
        """

        # DATA VALIDATION
        if numkinks < 1 or numkinks > 6:
            return await ctx.send("Please use a number from 1 to 6.")

        kink = random.sample(self.EXTREMEKINKLIST, k=numkinks)

        await ctx.send(', '.join(kink))

        return
