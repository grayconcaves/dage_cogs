from .cnoveltags import Cnoveltags


def setup(bot):
    bot.add_cog(Cnoveltags(bot))