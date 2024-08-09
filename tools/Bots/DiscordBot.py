import discord
from discord.ext import commands

def get_tokens():
    token_choice = input("Do you want to enter 1 token or 2 tokens? (Enter 1 or 2): ")
    
    if token_choice == '1':
        token = input("Please enter your bot token: ")
        return [token]
    elif token_choice == '2':
        token1 = input("Please enter the first bot token: ")
        token2 = input("Please enter the second bot token: ")
        return [token1, token2]
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return get_tokens()

tokens = get_tokens()

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
async def t_g_s(ctx):
    commands_list = """
    **Commands:**

    1. !ping

    2. !rm_all
    """
    await ctx.send(commands_list)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

# Run the bot(s) based on the number of tokens
for token in tokens:
    bot.run(token)
