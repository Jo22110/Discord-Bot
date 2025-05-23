from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='Returns the bot\'s latency')
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)  # Convert to milliseconds
        await ctx.send(f'🏓 Pong! Latency: {latency}ms')

    @commands.command(name='info', help='Displays information about the bot')
    async def info(self, ctx):
        embed = discord.Embed(title="Bot Information", color=discord.Color.blue())
        embed.add_field(name="Bot Name", value=self.bot.user.name, inline=True)
        embed.add_field(name="Bot ID", value=self.bot.user.id, inline=True)
        embed.add_field(name="Developer", value="Your Name", inline=True)
        embed.add_field(name="Version", value="1.0.0", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))