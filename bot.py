import discord
import asyncio
import sys
from os import environ as env_vars

client = discord.Client()

REACTION_CHANNEL_ID = ""
MOD_CHANNEL_ID = ""
REACTION_THRESHOLD = 5

try:
    REACTION_CHANNEL_ID = int(env_vars['DISCORD_REACTION_CHANNEL_ID'])
except KeyError:
    print("No Discord channel ID specified. Please set the DISCORD_REACTION_CHANNEL_ID environment variable.")
    sys.exit(1)

try:
    MOD_CHANNEL_ID = int(env_vars['DISCORD_MOD_CHANNEL_ID'])
except KeyError:
    MOD_CHANNEL_ID = REACTION_CHANNEL_ID

invisible = 'DISCORD_APPEAR_INVISIBLE' in env_vars

if 'DISCORD_REACTION_THRESHOLD' in env_vars:
    REACTION_THRESHOLD = int(env_vars['DISCORD_REACTION_THRESHOLD'])

    if REACTION_THRESHOLD < 1:
        print("Reaction threshold must be 2 or greater, to prevent the bot from reacting to itself.")
        sys.exit(1)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    
    if invisible:
        await client.change_presence(status=discord.Status.invisible)

async def send_feedback_embed(message):
    if message.author.id == client.user.id:
        return

    channel = client.get_channel(MOD_CHANNEL_ID)

    if not channel:
        print("Tried to send an embed to a nonexistent channel.")
        return

    embed = discord.Embed(title="New feedback received",
                          description=f"_You were notified about this feedback because it received at least {REACTION_THRESHOLD} upvotes._",
                          color=0x00ff00)
    embed.add_field(name="Feedback", value=message.content)

    await channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.channel.id == REACTION_CHANNEL_ID and message.author.id != client.user.id:
        await message.add_reaction('\N{THUMBS UP SIGN}')
        await message.add_reaction('\N{THUMBS DOWN SIGN}')

        def check(reaction, user):
            for r in reaction.message.reactions:
                if r.emoji == '\N{THUMBS UP SIGN}' and (r.count - 1) >= REACTION_THRESHOLD:
                    return True
            return False

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=86400.0, check=check)
            await send_feedback_embed(message)
        except asyncio.TimeoutError:
            return

try:
    client.run(env_vars['DISCORD_CLIENT_TOKEN'])
except KeyError:
    print("No Discord client token specified. Please set the DISCORD_CLIENT_TOKEN environment variable.")