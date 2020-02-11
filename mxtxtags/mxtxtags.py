# MXTX character/relationship tag generator cog for Dage

# Discord
import discord
import json
import re

# Red
from redbot.core import commands, Config
from redbot.core.data_manager import bundled_data_path


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



        
