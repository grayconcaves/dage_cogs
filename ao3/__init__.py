from .ao3 import Ao3


def setup(bot):
    bot.add_cog(Ao3(bot))