
import os
import discord

TOKEN = 

client = discord.Client()

# from discord.ext import commands
# bot = commands.Bot(command_prefix='+')

# @bot.event
# async def on_ready():
#     print(f'{client.user} test test')

# @bot.command(pass_context=True)
# async def birl(ctx):
#     await ctx.say('SAIU DA JAULA O MONSTRO')

@client.event
async def on_ready():
     print(f'{client.user} test test')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('+birl'):
        await message.channel.send('SAIU DA JAULA O MONSTRO')

client.run(TOKEN)