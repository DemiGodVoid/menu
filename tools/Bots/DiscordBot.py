import discord
from discord.ext import commands
import random
import asyncio  # Import asyncio module

TOKEN = input("Please enter your bot token: ")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Required to fetch members

bot = commands.Bot(command_prefix="!", intents=intents)

# Global variable to control spam loop
spam_active = False

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

    3. !spam (Works better with mulitple bots, say !stop to stop it)
    """
    await ctx.send(commands_list)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def spam(ctx):
    global spam_active
    spam_active = True
    messages = ["Hey", "NOOO", "BYE", "The Ghost Squad Team Says Hi.", "This server is under attack! Hide the kittens!!!!", "Even Banning me won't stop what comes next. hahahahahahhahahahahahahahahahahhahahahahhahahahahahahahahahahahahhahahaha"]
    while spam_active:
        message = random.choice(messages)  # Choose a random message
        await ctx.send(message)
        await asyncio.sleep(1)  # Wait for 1 second before sending the next message

@bot.command()
async def stop(ctx):
    global spam_active
    spam_active = False
    await ctx.send("Spam stopped.")

bot.run(TOKEN)
