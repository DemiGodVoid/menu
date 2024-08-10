import discord
from discord.ext import commands
import random
import asyncio

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

    1. !ping (checks if the bot is active)

    2. !rm_all (removes everyone from the discord server)

    3. !spam (spams random messages. say !stop to stop)

    4. !spam_dm @uservoid <text_here> (spam DMs the user, say !stop to stop)

    5. !add_channel <name> <amount> (creates specified number of channels with the given name)
    """
    await ctx.send(commands_list)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def spam(ctx):
    global spam_active
    spam_active = True
    messages = ["Hey", "NOOO", "BYE"]
    while spam_active:
        message = random.choice(messages)  # Choose a random message
        await ctx.send(message)
        await asyncio.sleep(1)  # Wait for 1 second before sending the next message

@bot.command()
async def stop(ctx):
    global spam_active
    spam_active = False
    await ctx.send("Spam stopped.")

@bot.command()
async def spam_dm(ctx, user: discord.User, *, message: str):
    # Check if the bot has permission to send DMs
    try:
        await user.send(message)
        await ctx.send(f"Started spamming {user.mention} with the message.")
        global spam_active
        spam_active = True
        
        while spam_active:
            await user.send(message)
            await asyncio.sleep(1)  # Wait for 1 second before sending the next message
            
    except Exception as e:
        await ctx.send(f"Failed to DM {user.mention}: {e}")

@bot.command()
@commands.has_permissions(manage_channels=True)  # Ensure only users with channel management permissions can use this command
async def add_channel(ctx, channel_name: str, amount: int):
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(f'{channel_name}-{i+1}')
            await asyncio.sleep(1)  # Wait 1 second between each channel creation to avoid rate limits
        except Exception as e:
            await ctx.send(f"Failed to create channel {channel_name}-{i+1}: {e}")
            break

    await ctx.send(f"{amount} channels named {channel_name} have been created.")

bot.run(TOKEN)
