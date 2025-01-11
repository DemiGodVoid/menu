import discord
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Enable member intents to fetch server members
client = discord.Client(intents=intents)

TOKEN = input("Please enter your Discord bot token: ")

# List of funny meme templates
meme_templates = [
    "{user1} got caught stealing {user2}'s lunch!",
    "{user1} Was caught sticking a dragon dildo up {user2}'s ass",
    "{user1} Is currently outside {user2}'s house with an AK-47, CALL THE COPS!",
    "{user1} Why are you currently watching porn inside your parents' bedroom closet with {user2}?",
    "{user1} Please stop playing footies with {user2}, that's your sister by blood.",
]

# Background task variables
meme_task = None
meme_interval = None

# List to store banned words
banned_words = []


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


async def send_meme_periodically(channel, interval):
    """Sends a meme periodically to the specified channel."""
    global meme_task
    while meme_task is not None:  # Ensure the task runs until explicitly stopped
        members = [member for member in channel.guild.members if not member.bot]
        if len(members) < 2:
            await channel.send("Not enough members to generate a meme!")
            return

        # Pick two random members
        user1, user2 = random.sample(members, 2)
        user1_mention = user1.mention
        user2_mention = user2.mention

        # Pick a random meme template
        meme = random.choice(meme_templates).format(user1=user1_mention, user2=user2_mention)
        await channel.send(meme)

        # Wait for the specified interval before sending the next meme
        await asyncio.sleep(interval * 60)


@client.event
async def on_message(message):
    global meme_task, meme_interval, banned_words

    if message.author == client.user:
        return

    # Check if the message contains a banned word
    for banned_word in banned_words:
        if banned_word in message.content.lower():
            await message.delete()
            return

    # Ping command
    if message.content == '!ping':
        await message.channel.send('PONG')

    # Commands list
    if message.content == '!commands':
        await message.channel.send(
            'Commands:\n\n!ping\n\n!gif text @user\n\n!meme\n\n!meme number (auto-send memes every X minutes)\n\n!stopmeme\n\n!bmessage word\n\n!unbmessage word\n\n!bannedwords'
        )

    # Meme command
    if message.content.startswith('!meme'):
        if message.content == '!meme':  # Single meme command
            members = [member for member in message.guild.members if not member.bot]
            if len(members) < 2:
                await message.channel.send("Not enough members to generate a meme!")
                return

            # Pick two random members
            user1, user2 = random.sample(members, 2)
            user1_mention = user1.mention
            user2_mention = user2.mention

            # Pick a random meme template
            meme = random.choice(meme_templates).format(user1=user1_mention, user2=user2_mention)
            await message.channel.send(meme)

        elif message.content.startswith('!meme '):  # Auto-meme command
            try:
                interval = int(message.content.split(' ')[1])
                if interval < 1:
                    await message.channel.send("Please enter a number greater than 0.")
                    return

                meme_interval = interval
                if meme_task is not None:
                    meme_task.cancel()  # Cancel any existing auto-meme task
                meme_task = asyncio.create_task(send_meme_periodically(message.channel, meme_interval))
                await message.channel.send(f"Auto-memes enabled. A meme will be sent every {meme_interval} minute(s).")

            except ValueError:
                await message.channel.send("Invalid format. Use: !meme number")

    # Stop auto-meme command
    if message.content == '!stopmeme':
        if meme_task is not None:
            meme_task.cancel()
            meme_task = None
            await message.channel.send("Auto-memes disabled.")
        else:
            await message.channel.send("Auto-memes are not currently running.")

    # Bmessage command to add a banned word
    if message.content.startswith('!bmessage'):
        await message.delete()
        word_to_ban = message.content[len('!bmessage '):].strip().lower()
        if not word_to_ban:
            await message.channel.send("Please specify a word to ban. Usage: !bmessage <word>")
        elif word_to_ban in banned_words:
            await message.channel.send(f"`{word_to_ban}` is already banned!")
        else:
            banned_words.append(word_to_ban)
            await message.channel.send(f"`{word_to_ban}` has been added to the banned words list!")

    # Unbmessage command to remove a banned word
    if message.content.startswith('!unbmessage'):
        word_to_unban = message.content[len('!unbmessage '):].strip().lower()
        if not word_to_unban:
            await message.channel.send("Please specify a word to unban. Usage: !unbmessage <word>")
        elif word_to_unban not in banned_words:
            await message.channel.send(f"`{word_to_unban}` is not in the banned words list!")
        else:
            banned_words.remove(word_to_unban)
            await message.channel.send(f"`{word_to_unban}` has been removed from the banned words list!")

    # List all banned words
    if message.content == "!bannedwords":
        if not banned_words:
            await message.channel.send("No words are currently banned.")
        else:
            await message.channel.send(f"Banned words: {', '.join(banned_words)}")


client.run(TOKEN)
