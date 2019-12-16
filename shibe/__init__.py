from .shibe import Shibe


def setup(bot):
    bot.add_cog(Shibe(bot))