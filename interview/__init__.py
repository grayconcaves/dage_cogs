from .interview import Interview


def setup(bot):
    bot.add_cog(Interview(bot))