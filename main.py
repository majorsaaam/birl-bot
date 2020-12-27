import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='+')


@bot.command()
async def birl(ctx, arg1, arg2):
    await ctx.send('SAIU DA JAULA O MONSTRO {} - e ce passou {} e {}'.format(ctx.author, arg1, arg2))


bot.run(TOKEN)