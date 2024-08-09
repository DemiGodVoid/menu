import discord
from discord.ext import commands

# Prompt the user to input the bot's token
TOKEN = input("Please enter your bot token: ")

intents = discord.Intents.default()
intents.message_content = True  # Ensures bot can read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong')

# Run the bot with the provided token
bot.run(TOKEN)
