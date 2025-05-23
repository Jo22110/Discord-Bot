import discord
from discord.ext import commands
import os

# Load configuration settings
from .config.settings import TOKEN, PREFIX

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Load cogs
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')
    for filename in os.listdir('./bot/cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded cog: {filename[:-3]}')

# Start the bot
bot.run(TOKEN)