from .thesaurus import Thesaurus


def setup(bot):
    bot.add_cog(Thesaurus(bot))