import discord
from discord.ext import commands
import random  # Import random module for random choice

TOKEN = input("Please enter your bot token: ")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Required to fetch members

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
@commands.has_permissions(administrator=True)  # Ensures only admins can use this command
async def rm_all(ctx):
    if ctx.author == ctx.guild.owner:
        await ctx.send("Kicking all members...")
        for member in ctx.guild.members:
            if member != ctx.guild.owner and not member.bot:  # Don't kick the owner or bots
                try:
                    await member.kick(reason="Server restart")
                    print(f"Kicked {member.name}")
                except Exception as e:
                    print(f"Failed to kick {member.name}: {e}")
        await ctx.send("All members have been kicked.")
    else:
        await ctx.send("Only the server owner can use this command.")

@bot.command()
async def tgs(ctx):
    commands_list = """
    **Commands:**

    1. !ping

    2. !rm_all
    """
    await ctx.send(commands_list)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def spam(ctx):
    messages = ["Hey", "NOOO", "BYE"]
    while True:
        message = random.choice(messages)  # Choose a random message
        await ctx.send(message)
        await asyncio.sleep(1)  # Wait for 1 second before sending the next message

bot.run(TOKEN)
