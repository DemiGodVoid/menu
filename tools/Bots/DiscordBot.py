import discord
from discord.ext import commands
import asyncio

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

class BotClient(commands.Bot):
    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    @commands.command()
    @commands.has_permissions(administrator=True)  # Ensures only admins can use this command
    async def rm_all(self, ctx):
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

    @commands.command()
    async def t_g_s(self, ctx):
        commands_list = """
        **Commands:**

        1. !ping

        2. !rm_all
        """
        await ctx.send(commands_list)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

async def main():
    tokens = get_tokens()
    tasks = []
    
    for token in tokens:
        bot = BotClient(token, command_prefix="!", intents=discord.Intents.default())
        bot.intents.message_content = True
        bot.intents.members = True
        tasks.append(bot.start(token))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
