from discord.ext import commands
import discord

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play', help='Plays a song from a given URL')
    async def play(self, ctx, url: str):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            voice_client = await channel.connect()
            # Here you would add the logic to play the music from the URL
            await ctx.send(f'Now playing: {url}')
        else:
            await ctx.send("You need to be in a voice channel to play music.")

    @commands.command(name='stop', help='Stops the currently playing music')
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Music stopped and disconnected from the voice channel.")
        else:
            await ctx.send("I'm not connected to a voice channel.")

    @commands.command(name='pause', help='Pauses the currently playing music')
    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("Music paused.")
        else:
            await ctx.send("No music is currently playing.")

    @commands.command(name='resume', help='Resumes the paused music')
    async def resume(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("Music resumed.")
        else:
            await ctx.send("No music is currently paused.")

def setup(bot):
    bot.add_cog(Music(bot))