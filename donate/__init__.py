from .donate import Donate


def setup(bot):
    bot.add_cog(Donate(bot))