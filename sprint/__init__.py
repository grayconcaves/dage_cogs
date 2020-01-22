from .sprint import Sprint


def setup(bot):
    bot.add_cog(Sprint(bot))