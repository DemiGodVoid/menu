import discord
from discord.ext import commands
import asyncio

def get_tokens_and_channels():
    token_choice = input("Do you want to enter 1 token or 2 tokens? (Enter 1 or 2): ")
    
    if token_choice == '1':
        token = input("Please enter your bot token: ")
        channel_id = int(input("Please enter the channel ID for the bot to talk in: "))
        return [(token, channel_id)]
    elif token_choice == '2':
        token1 = input("Please enter the first bot token: ")
        channel_id1 = int(input("Please enter the channel ID for the first bot to talk in: "))
        token2 = input("Please enter the second bot token: ")
        channel_id2 = int(input("Please enter the channel ID for the second bot to talk in: "))
        return [(token1, channel_id1), (token2, channel_id2)]
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return get_tokens_and_channels()

class BotClient(commands.Bot):
    def __init__(self, token, channel_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.channel_id = channel_id

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(self.channel_id)
        if channel:
            await channel.send("Hello! I am now online.")
        else:
            print(f"Channel with ID {self.channel_id} not found.")

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
    tokens_and_channels = get_tokens_and_channels()
    tasks = []
    
    for token, channel_id in tokens_and_channels:
        bot = BotClient(token, channel_id, command_prefix="!", intents=discord.Intents.default())
        bot.intents.message_content = True
        bot.intents.members = True
        tasks.append(bot.start(token))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
