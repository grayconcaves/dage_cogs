# Ao3 cog for Dage

# Discord
import discord

# Red
from redbot.core import commands, checks, Config
from redbot.core.utils.chat_formatting import humanize_list
from redbot.core.utils import deduplicate_iterables
from redbot.core.utils.predicates import MessagePredicate, ReactionPredicate
from redbot.core.utils.menus import start_adding_reactions

# Libs
import asyncio
import aiohttp
from bs4 import BeautifulSoup, SoupStrainer

class Ao3(commands.Cog):
    """Ao3 commands"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.config = Config.get_conf(self, identifier=9657852, force_registration=True)
        self.config.register_guild(
            autodelete=False,
            censor=True,
            embed=False,
            pairlimit=3,
            taglimit=5,
            fandomlimit=1,
            noteslimit=500,
            sumlimit=1500,
            defaultformat="**{title}** by **{authors}**\n{url}\n**Fandoms:** {fandom}\n**Rating:** {rating}     **Warnings:** {warnings}\n**Relationships:** {pairing}\n**Tags:** {tags}\n**Summary:** {summary}**Words:** {words}     **Chapters:** {totalchapters}\n**Notes by {reccer}**: {notes}",
            formatting="Title: **__{title}__**\nAuthor: {authors}\nFandom: {fandom}\nPairing: {pairing}\nRating: {rating}\nWarning: {warnings}\n\nSummary: {summary}\nTags: {tags}\nChapters: {totalchapters}\n\nRecced by {reccer} {notes} \nRead it here: {url}"         
        )
    
    @commands.guild_only()
    @commands.command()
    async def ao3(self, ctx, ficlink, *, notes=""):
        """Returns details of a fic from a link

        If the fic you inputted is wrong, just click the ❎ emoji to delete the message (Needs Manage Messages permissions)."""      

        # SET NOTES
        if notes == "":
            notes = "None."
        else:
            nlimit = await self.config.guild(ctx.guild).noteslimit()
            notes = notes[:nlimit]
        
        # GET URL
        if "chapter" in ficlink:
            newlink = ficlink.split("chapters")[0]
            ficlink = str(newlink)
        if "collections" in ficlink:
            newlink = ficlink.split("/works/")[1]
            ficlink = str(f"https://archiveofourown.org/works/{newlink}")


        firstchap = f"{ficlink}/navigate"
        async with self.session.get(firstchap) as ao3navigation:
            navigate = BeautifulSoup(await ao3navigation.text(), 'html.parser', parse_only=SoupStrainer("ol"))
        firstchap = navigate.find("li").a['href']
        url = f"https://archiveofourown.org{firstchap}?view_adult=true"

        # START SCRAPING
        async with self.session.get(url) as ao3session:
            result = BeautifulSoup(await ao3session.text(), 'html.parser')
    
        # GET AUTHORS
        try:
            a = result.find_all("a", {'rel': 'author'})
            author_list = []
            for author in a:
                author_list.append(author.string.strip())
            try:
                authors = humanize_list(deduplicate_iterables(author_list))
            except Exception:
                authors = "Anonymous"
        except Exception:
            return await ctx.send("Error loading author list.")
    
        # GET TITLE
        try:
            preface = result.find("div", {'class': 'preface group'}).h2.string
            title = str(preface.strip())
        except Exception:
            title = "No title found."

        # GET FANDOM
        try:
            fan = result.find("dd", {'class': 'fandom tags'})
            fan_list = []
            fandomlimit = await self.config.guild(ctx.guild).fandomlimit()
            for fandom in fan.find_all("li", limit=fandomlimit):
                fan_list.append(fandom.a.string)
            fandom = humanize_list(fan_list)
        except Exception:
            fandom = "No fandom found."
        
        # GET PAIRING
        try:
            reltags = result.find("dd", {'class': 'relationship tags'})
            pair_list = []
            pairlimit = await self.config.guild(ctx.guild).pairlimit()
            for rel in reltags.find_all("li", limit=pairlimit):
                pair_list.append(rel.a.string)
            pairing = humanize_list(pair_list)
        except Exception:
            pairing = "No Pairing."

        # GET CHAPTERS
        chapters = result.find("dd", {'class': 'chapters'})
        totalchapters = str(BeautifulSoup.getText(chapters))

        # GET STATUS
        chap_list = totalchapters.split("/")
        if "?" in chap_list[1]:
            status = "Work in Progress"
        elif chap_list[0] != chap_list[1]:
            status = "Work in Progress"
        else:
            status = "Complete"

        # GET RATING
        try:
            rate = result.find("dd", {'class': 'rating tags'})
            rating = rate.a.string
        except Exception:
            rating = "Not Rated"

        # GET SUMMARY
        try:
            div = result.find("div", {'class': 'preface group'})
            userstuff = div.find("blockquote", {'class': 'userstuff'})
            stuff = str(BeautifulSoup.getText(userstuff))
            summarytest = f"{stuff}".replace('. ', '**').replace('.', '. ')
            summ = f"{summarytest}".replace('**', '. \n\n')
            slimit = await self.config.guild(ctx.guild).sumlimit()
            summary = summ[:slimit]
        except Exception:
            summary = "No work summary found." 

        # GET TAGS
        try:
            use_censor = await self.config.guild(ctx.guild).censor()
            freeform = result.find("dd", {'class': 'freeform tags'})
            tag_list = []
            taglimit = await self.config.guild(ctx.guild).taglimit()
            for tag in freeform.find_all("li", limit=taglimit):
                tag_list.append(tag.a.string)
            if "Explicit" in rating and use_censor:
                tags = f"||{(humanize_list(tag_list))}||"
            else:
                tags = humanize_list(tag_list)

        except Exception:
            tags = "No tags found."

        # GET DATE PUBLISHED AND UPDATED
        published = result.find("dd", {'class': 'published'}).string.strip()
        try:
            updated = result.find("dd", {'class': 'status'}).string.strip()
        except Exception:
            updated = published

        # GET LANGUAGE
        language = result.find("dd", {'class': 'language'}).string.strip()

        # GET WORDS
        words = int(result.find("dd", {'class': 'words'}).string.replace(",",""))

        # GET KUDOS
        kudos = int(result.find("dd", {'class': 'kudos'}).string.replace(",",""))

        # GET HITS
        hits = int(result.find("dd", {'class': 'hits'}).string.replace(",",""))

        # GET WARNINGS
        warntags = result.find("dd", {'class': 'warning tags'})
        warn_list = []
        try:
            for warning in warntags.find_all("li"):
                warn_list.append(warning.a.string)
            warnings = humanize_list(warn_list)
        except Exception:
            warnings = "No warnings found."
            
        # CHECK INFO FORMAT
        use_embed = await self.config.guild(ctx.guild).embed()
        data = await self.config.guild(ctx.guild).formatting()

        if use_embed:
            data = discord.Embed(description=summary, title=title, url=ficlink, colour=3553599)
            data.add_field(name="Author:", value=authors, inline=False)
            data.add_field(name="Fandom:", value=fandom, inline=False)
            data.add_field(name="Rating:", value=rating, inline=False)
            data.add_field(name="Pairings:", value=pairing, inline=False)
            data.add_field(name="Tags:", value=tags, inline=False)
            data.add_field(name= f"Rec Notes by {ctx.author}: ", value=notes, inline=False)
            data.set_footer(text= f"Language: {language}     |       Words: {words}       |       Date Updated: {updated}        |       Status: {status}        ")
            ao3msg = await ctx.send(embed=data)

        else:
            params = {
                "title": title, 
                "authors": authors, 
                "rating": rating, 
                "warnings": warnings, 
                "language": language,
                "fandom": fandom, 
                "pairing": pairing, 
                "tags": tags, 
                "summary": summary,
                "totalchapters": totalchapters,
                "status": status, 
                "words": words,
                "kudos": kudos,
                "hits": hits, 
                "reccer" : ctx.author.mention,
                "notes": notes,
                "url": f"<{ficlink}>",
                "published": published,
                "updated": updated
            }
            ao3msg = await ctx.send(data.format(**params))

        start_adding_reactions(ao3msg, ReactionPredicate.YES_OR_NO_EMOJIS)

        pred = ReactionPredicate.yes_or_no(ao3msg, ctx.author)
        try:
            await ctx.bot.wait_for("reaction_add", check=pred, timeout=30)
            await self._clear_react(ao3msg)

            if pred.result is False:
                await ao3msg.delete()
                return

        except asyncio.TimeoutError:
            await self._clear_react(ao3msg)

        autodel = await self.config.guild(ctx.guild).autodelete()
 
        try:
            if autodel is True:
                await ctx.message.delete()
            return
        except Exception:
            return
   


    @commands.command(aliases=['formatao3'])
    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    async def ao3format(self, ctx, *, formatstring):
        """Customize your ao3 blurb's PLAIN TEXT format."""

        oldformat = await self.config.guild(ctx.guild).formatting()

        if "RESET" in formatstring:
            formatstring = await self.config.guild(ctx.guild).defaultformat()
            await ctx.send("Format has been reset to default.")

        await self.config.guild(ctx.guild).formatting.set(formatstring)
        await ctx.send("New format has been set.")
        await ctx.send(f"```{formatstring}```")
        return

    @commands.group(aliases=['helpformat'])
    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    async def formathelp(self, ctx):
        """Tutorial for formatting.
        
To reset to default formatting, use RESET. i.e. `[p]ao3format RESET`

To specify the work info and format that you want to show on your server: `[p]ao3format <custom formatting>`

You can use the following parameters for your ao3 info:
```url, title, authors, rating, warnings, language, fandom, pairing, tags, summary, totalchapters, status, words, kudos, hits, published, updated, notes, reccer```

To format the message with these parameters, include them in your message encased in curly braces {}
You can also add whitespace (using Shift+Enter) as well as use Discord's native formatting.
        
For example:
```[p]ao3format\n**{title}** by {authors}.\nPairing: {pairing}\nRating: {rating}\nTags: {tags}\n\nSummary: \n{summary}```
Result:
```**Title** by Author. \nPairing: Pairing(s) \nRating: Rating \nTags: Tag 1, Tag 2, Tag 3, Tag 4, Tag 5\n\nSummary:\nsummary```
"""
        pass

    @formathelp.command(aliases=['c'])
    async def current(self, ctx):
        """See and preview your current formatting."""


        currentformat = await self.config.guild(ctx.guild).formatting()
        await ctx.send(f"Current formatting:```css\n{currentformat}```")
        preview = await ctx.send("Do you want to preview your ao3 work card with this format?")

        start_adding_reactions(preview, ReactionPredicate.YES_OR_NO_EMOJIS)

        pred = ReactionPredicate.yes_or_no(preview, ctx.author)
        try:
            await ctx.bot.wait_for("reaction_add", check=pred, timeout=30)

            if pred.result is True:
                await preview.delete()
                params = {
                    "title": "Title", 
                    "authors": "Authors", 
                    "rating": "Rating", 
                    "warnings": "Warnings", 
                    "language": "Language",
                    "fandom": "Fandom", 
                    "pairing": "Pairing", 
                    "tags": "Tags", 
                    "summary": "Summary",
                    "totalchapters": "Chapters",
                    "status": "Status", 
                    "words": "Words",
                    "kudos": "Kudos",
                    "hits": "Hits",
                    "published": "Date Published",
                    "updated": "Date Updated", 
                    "reccer" : "@/person",
                    "notes": "Notes",
                    "url": "<Link Here>",
                }
                previewmsg = await ctx.send(currentformat.format(**params))          

            else:
                await preview.delete()

        except asyncio.TimeoutError:
            await preview.delete()      

        return

    @formathelp.command(aliases=['d'])
    async def default(self, ctx):
        """See default bot formatting."""

        defaultformat = await self.config.guild(ctx.guild).defaultformat()
        await ctx.send(f"Default formatting:```css\n{defaultformat}```")



    @commands.group(aliases=['setao3'])
    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    async def ao3set(self, ctx):
        """Set how the Ao3 work info card is displayed in your guild."""
        pass

    @ao3set.command(aliases=['delete'])
    async def autodelete(self, ctx):
        """Toggle if the previous message auto deletes. Needs Manage Messages Permission."""
        auto = await self.config.guild(ctx.guild).autodelete()
        await self.config.guild(ctx.guild).autodelete.set(not auto)
        return await ctx.send(f"Deletion of the original message has been set to **{not auto}**.")

    @ao3set.command(aliases=['censors', 'spoiler', 'spoilers'])
    async def censor(self, ctx):
        """Toggle the spoiler/censor of an Explicit work's tags."""
        censors = await self.config.guild(ctx.guild).censor()
        await self.config.guild(ctx.guild).censor.set(not censors)
        return await ctx.send(f"Spoiler/censors of an Explicit fic's tags have been set to **{not censors}**.")

    @ao3set.command(aliases=['embed'])
    async def embeds(self, ctx):
        """Toggle using an embed or just plain text."""
        toggle = await self.config.guild(ctx.guild).embed()
        await self.config.guild(ctx.guild).embed.set(not toggle)
        return await ctx.send(f"Embeds have been set to **{not toggle}**.")

    @ao3set.command(aliases=['tags', 'maxtags'])
    async def tag(self, ctx, maxtags):
        """Set a maximum limit for additional tags"""
        try:
            maxtags = int(maxtags)
        except Exception:
            await ctx.send("Please use a number.")
        if maxtags < 1:
            await ctx.send("Please use a number greater than 1.")
        else:
            await self.config.guild(ctx.guild).taglimit.set(maxtags)
            await ctx.send(f"Your new addtional tags limit is **{maxtags}**.")
        return

    @ao3set.command(aliases=['pairing', 'pair', 'relationship', 'relationships', 'reltags', 'rel', 'maxpairtags'])
    async def pairs(self, ctx, maxpairtags):
        """Set a maximum limit for pairing/relationship tags"""
        try:
            maxpairtags = int(maxpairtags)
        except Exception:
            await ctx.send("Please use a number.")
        if maxpairtags < 1:
            await ctx.send("Please use a number greater than 1.")
        else:
            await self.config.guild(ctx.guild).pairlimit.set(maxpairtags)
            await ctx.send(f"Your new relationship tags limit is **{maxpairtags}**.")
        return

    @ao3set.command(aliases=['fandoms', 'fandomtags', 'maxfandomtags'])
    async def fandom(self, ctx, maxfandomtags):
        """Set a maximum limit for fandom tags"""
        try:
            maxfandomtags = int(maxfandomtags)
        except Exception:
            await ctx.send("Please use a number.")
        if maxfandomtags < 1:
            await ctx.send("Please use a number greater than 1.")
        else:
            await self.config.guild(ctx.guild).fandomlimit.set(maxfandomtags)
            await ctx.send(f"Your new fandom tags limit is **{maxfandomtags}**.")
        return

    @ao3set.command(aliases=['note'])
    async def notes(self, ctx, notelimit: int):
        """Set a maximum limit for user notes."""
        if notelimit < 0 or notelimit > 500:
            await ctx.send("Please use a positive number less than 500")
        else:
            await self.config.guild(ctx.guild).noteslimit.set(notelimit)
            await ctx.send(f"You new notes character limit is **{notelimit}**")
        return

    @ao3set.command(aliases=['sum'])
    async def summary(self, ctx, summarylimit: int):
        """Set a maximum limit for fic summaries."""
        if summarylimit < 0 or summarylimit > 1500:
            await ctx.send("Please use a positive number less than 1500")
        else:
            await self.config.guild(ctx.guild).sumlimit.set(summarylimit)
            await ctx.send(f"You new summary character limit is **{summarylimit}**")
        return


    @staticmethod
    async def _clear_react(msg):
        try:
            await msg.clear_reactions()
            return
        except discord.errors.Forbidden:
            pass

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())
