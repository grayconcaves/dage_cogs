# thesaurus cog for dage

# Discord
import discord
import re

# Red
from redbot.core import commands

# Libs
import aiohttp

class Thesaurus(commands.Cog):
    """Access the thesaurus.

    Dictionary used: Datamuse API"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()


    @commands.command(aliases=['syn'])
    async def synonym(self, ctx, word, topic=""):
        """Get a word's synonyms.

        Optional: include a topic to choose words from."""
        if topic != "":
            topics = f"&topics={topic}"
            topic = f" regarding **{topic}**"
        else:
            topics = ""

        try:
            async with self.session.get(f"https://api.datamuse.com/words?rel_syn={word}{topics}&max=30") as s:
                syns = await s.json()
        except (ValueError, AttributeError, NameError):
            return await ctx.send("Error.")

        await ctx.send(f"Synonyms for **{word}**{topic}:\n\n{', '.join(self.get_results(syns))}")
        return



    @commands.command(aliases=['ant'])
    async def antonym(self, ctx, word, topic=""):
        """Get a word's antonyms.

        Optional: include a topic to choose words from."""
        if topic != "":
            topics = f"&topics={topic}"
            topic = f" regarding **{topic}**"
        else:
            topics = ""

        try:
            async with self.session.get(f"https://api.datamuse.com/words?rel_ant={word}{topics}&max=30") as a:
                ants = await a.json()
        except (ValueError, AttributeError, NameError):
            return await ctx.send("Error.")

        await ctx.send(f"Antonyms for **{word}**{topic}:\n\n{', '.join(self.get_results(ants))}")
        return



    @commands.command(aliases=['desc','d'])
    async def describe(self, ctx, word, topic=""):
        """Get adjectives for a word.

        Optional: include a topic to choose words from."""
        if topic != "":
            topics = f"&topics={topic}"
            topic = f" regarding **{topic}**"
        else:
            topics = ""

        try:
            async with self.session.get(f"https://api.datamuse.com/words?rel_jjb={word}{topics}&max=30") as ad:
                adjs = await ad.json()
        except (ValueError, AttributeError, NameError):
            return await ctx.send("Error.")

        await ctx.send(f"Adjectives for **{word}**{topic}:\n\n{', '.join(self.get_results(adjs))}")
        return


    @commands.command(aliases=['dby','descby'])
    async def describedby(self, ctx, word, topic=""):
        """Get nouns described by an adjective.

        Optional: include a topic to choose words from."""
        if topic != "":
            topics = f"&topics={topic}"
            topic = f" regarding **{topic}**"
        else:
            topics = ""

        try:
            async with self.session.get(f"https://api.datamuse.com/words?rel_jja={word}{topics}&max=30") as nn:
                nouns = await nn.json()
        except (ValueError, AttributeError, NameError):
            return await ctx.send("Error.")

        await ctx.send(f"Nouns described by **{word}**{topic}:\n\n{', '.join(self.get_results(nouns))}")
        return


    @commands.command()
    async def rhyme(self, ctx, word, topic=""):
        """Get rhymes for a word.

        Optional: include a topic to choose words from."""
        if topic != "":
            topics = f"&topics={topic}"
            topic = f" regarding **{topic}**"
        else:
            topics = ""

        try:
            async with self.session.get(f"https://api.datamuse.com/words?rel_rhy={word}{topics}&max=30") as rhy:
                rhyme = await rhy.json()
        except (ValueError, AttributeError, NameError):
            return await ctx.send("Error.")

        await ctx.send(f"Words rhyming with **{word}**{topic}:\n\n{', '.join(self.get_results(rhyme))}")
        return


    @commands.command()
    async def related(self, ctx, word, topic=""):
        """Find words associated to your word.

        Optional: include a topic to choose words from."""
        if topic != "":
            topics = f"&topics={topic}"
            topic = f" regarding **{topic}**"
        else:
            topics = ""

        try:
            async with self.session.get(f"https://api.datamuse.com/words?rel_trg={word}{topics}&max=30") as rel:
                related = await rel.json()
        except (ValueError, AttributeError, NameError):
            return await ctx.send("Error.")

        await ctx.send(f"Words associated with **{word}**{topic}:\n\n{', '.join(self.get_results(related))}")
        return


    @commands.command(aliases=['wsearch'])
    async def wordsearch(self, ctx, *, description):
        """Find the word that suits your needs.

        Use the following flags separated by commas to further specify your search:
        `means like` or `ml` - Find words that fit the meaning you want to portray.
        `sounds like` or `sl` - Find words that sound like your word
        `spelled like` or `sp` - Finds words spelled similar to that word.

        Only the top five results will be shown, sorted according to accuracy.

        Examples:
        [p]wsearch means like ringing in the ears, sounds like teeny toes, spelled like tinnies
        > tinnitus

        [p]wsearch ml tall animal, sl jiraff
        > giraffe, jeer, carafe
        """
        param = re.sub(r'means like |ml ','ml=', description)
        param = re.sub(r'sounds like |sl ','sl=', param)
        param = re.sub(r'spelled like |sp ','sp=', param)
        param = re.sub(r', ', '&', param)
        param = re.sub(r' ', '+', param)

        try:
            async with self.session.get(f"https://api.datamuse.com/words?{param}&max=5") as ws:
                wsearch = await ws.json()
        except (ValueError, AttributeError):
            return await ctx.send("Error.")

        await ctx.send(f"Possible words:\n\n{', '.join(self.get_results(wsearch))}")
        return


    def get_results(self, json):
        result_list = []
        y = len(json)
        for x in range(y):
            r = json[x]['word']
            result_list.append(r)
        if result_list == []:
            result_list = ['No results found.']
        return result_list


    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())