from .twtid import Twtid


def setup(bot):
    bot.add_cog(Twtid(bot))