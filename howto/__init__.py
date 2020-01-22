from .howto import Howto


def setup(bot):
    bot.add_cog(Howto(bot))