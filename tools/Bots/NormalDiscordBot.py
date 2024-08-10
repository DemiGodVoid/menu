import discord
import requests
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = input("Please enter your Discord bot token: ")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!ping':
        await message.channel.send('PONG')

    if message.content.startswith('!gif '):
        parts = message.content.split(' ', 2)
        if len(parts) == 3 and parts[1] and parts[2]:
            text = parts[1]
            mentioned_user = parts[2]
            sender = message.author.mention
            
            gif_url = search_gif(text)
            if gif_url:
                await message.channel.send(f'{mentioned_user}, here\'s a {text} from {sender}!', file=discord.File(fp=requests.get(gif_url, stream=True).raw, filename='image.gif'))
            else:
                await message.channel.send('No GIF found!')

def search_gif(query):
    url = f'https://api.giphy.com/v1/gifs/translate?s={query}&api_key=dc6zaTOxFJmzC'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'images' in data['data']:
            return data['data']['images']['original']['url']
    return None

client.run(TOKEN)
