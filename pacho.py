import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

client = discord.Client()  #connection to discord

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

@client.event #event registry
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'Todopoderosa {client.user} ha llegado a {guild.name}\n')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("Grandísima Pacho"):
        await message.channel.send("...")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Estimado/a {member.name}, Pacho envía sus saludos.'
    )




client.run(TOKEN)
