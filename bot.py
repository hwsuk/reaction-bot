import discord
from os import environ as env_vars

client = discord.Client()

CHANNEL_ID = ""

try:
    CHANNEL_ID = env_vars['DISCORD_CHANNEL_ID']
except KeyError:
    print("No Discord channel ID specified. Please set the DISCORD_CHANNEL_ID environment variable.")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if(message.channel.id == CHANNEL_ID):
        await message.add_reaction('\N{THUMBS UP SIGN}')
        await message.add_reaction('\N{THUMBS DOWN SIGN}')

try:
    client.run(env_vars['DISCORD_CLIENT_TOKEN'])
except KeyError:
    print("No Discord client token specified. Please set the DISCORD_CLIENT_TOKEN environment variable.")