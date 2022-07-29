import discord
import os
import TalkToChuck as ttc
from keep_alive import keep_alive


discord_bot_token = os.environ.get('DISCORD_CHUCK_NORRIS_BOT_TOKEN')
discord_channel = os.environ.get('DISCORD_CHUCK_NORRIS_CHANNEL')

client = discord.Client()


@client.event
async def on_ready():
    print('bot online')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != int(discord_channel):
        return

    msg = str(message.content).lower()
    greeting_words = ['hello', 'hey', 'yo']

    if "$categories" in msg.split():
        categories = ttc.get_categories()
        chuck_response = 'Here are categories that Chuck likes to joke about:\n\n'
        for category in categories:
            chuck_response += f'{category}\n'
        await message.channel.send(chuck_response)
        return

    if 'chuck' in msg.split():
        chuck_response = f"That's Mr. Norris to you, {message.author}. I won't remind you again!"
        await message.channel.send(chuck_response)
        return

    if any(word in msg for word in greeting_words):
        chuck_response = f'Hello {message.author}!'
        await message.channel.send(chuck_response)

    category_found = False
    joke = None

    if 'joke' in msg:
        for word in msg.split():
            categories = ttc.get_categories()
            if word in categories:
                joke = ttc.get_joke(category=word)
                category_found = True
        if not category_found:
            joke = ttc.get_random_joke()
        chuck_response = f"Here's a {joke['categories'][0]} joke that makes me laugh: {joke['value']}"
        await message.channel.send(chuck_response)


keep_alive()
client.run(discord_bot_token)
