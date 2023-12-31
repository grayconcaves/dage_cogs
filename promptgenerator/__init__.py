from .promptgen import Promptgen


async def setup(bot):
    await bot.add_cog(Promptgen(bot))
