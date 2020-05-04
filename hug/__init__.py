from .hug import Hug


def setup(bot):
    bot.add_cog(Hug(bot))