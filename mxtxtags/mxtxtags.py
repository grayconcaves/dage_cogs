# MXTX character/relationship tag generator cog for Dage

# Discord
import discord
import json
import re
import random

# Red
from redbot.core import commands, Config
from redbot.core.data_manager import bundled_data_path
from redbot.core.utils.chat_formatting import humanize_list


class Mxtxtags(commands.Cog):
    """Convert MXTX fandom names to Ao3-format tags"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=79797979795641, force_registration=True)
        
        tag_fp = bundled_data_path(self) / "taglist.json"
        with tag_fp.open("r", encoding='utf-8') as tagses:
            self.TAGLIST = json.load(tagses)

    @commands.command(aliases=['mxtxtags','tag', 'cntag'])
    async def mxtxtag(self, ctx, *, tags):
        """Replace fandom/unmarked pinyin names with Ao3's format

Ao3 still uses pinyin with tone marks/diacritics for most MXTX characters and relationships.

This cog will convert most common fandom nicknames into Ao3's format, which you can then easily paste into Ao3's Character or Relationship tags boxes.

e.g.
```[p]mxtxtag wwx, bingqiu, hc/xl```
will return
```Wèi Yīng | Wèi Wúxiàn, Luò Bīnghé/Shěn Yuán | Shěn Qīngqiū, Huā Chéng/Xiè Lián```

        """
        tl = re.split("(\W+)", tags.lower())
        ao3list = []
        for tag in tl:
            ao3list.append(self.TAGLIST.get(tag, tag))
        await ctx.send(''.join(ao3list))
        return
    
    @commands.command(aliases=['pairgen','mxtxpair'])
    async def pairgenerator(self, ctx, fandom:str = "all", numpairs:int = 2):
        """Generate a random MXTX pairing! 

To generate less or more a pair, just include a number from 1 to 5. 

To limit to a fandom, just add ONLY one of the fandom flags: `mdzs` | `sv` | `tgcf` | `all`

        """

        if numpairs > 5 or numpairs < 1:
        	return await ctx.send("Please input a valid number from 1 to 5")

        if fandom == "all":
        	pairs = random.choices(list(self.TAGLIST.values())[0:84], k=numpairs)
        elif fandom == "mdzs":
        	pairs = random.choices(list(self.TAGLIST.values())[0:37], k=numpairs)
        elif fandom == "sv":
        	pairs = random.choices(list(self.TAGLIST.values())[38:58], k=numpairs)
        elif fandom == "tgcf":
        	pairs = random.choices(list(self.TAGLIST.values())[59:84], k=numpairs)
        else:
        	return await ctx.send("Please input a valid fandom.")

        await ctx.send('/'.join(pairs))
        return

    @commands.command(aliases=['chargen','mxtxchar'])
    async def chargenerator(self, ctx, fandom:str = "all", numchars:int = 1):
        """Generate a random MXTX character! 

You can generate at most 5 characters. 

To limit to a fandom, just add ONLY one of the fandom flags: `mdzs` | `sv` | `tgcf` | `all`

        """

        if numchars > 5 or numchars < 1:
        	return await ctx.send("Please input a valid number from 1 to 5")

        if fandom == "all":
        	chars = random.sample(list(self.TAGLIST.values())[0:84], k=numchars)
        elif fandom == "mdzs":
        	chars = random.sample(list(self.TAGLIST.values())[0:37], k=numchars)
        elif fandom == "sv":
        	chars = random.sample(list(self.TAGLIST.values())[38:58], k=numchars)
        elif fandom == "tgcf":
        	chars = random.sample(list(self.TAGLIST.values())[59:84], k=numchars)
        else:
        	return await ctx.send("Please input a valid fandom.")

        await ctx.send(humanize_list(chars))
        return



        
