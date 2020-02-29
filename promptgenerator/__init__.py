from .promptgen import Promptgen


def setup(bot):
    bot.add_cog(Promptgen(bot))