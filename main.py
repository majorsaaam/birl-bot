import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from exercicio import Exercicio
from scoreboard import Scoreboard

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client()
scoreboard = Scoreboard()
bot = commands.Bot(command_prefix='+')

@bot.command()
async def birl(ctx, *args):
    # await ctx.send('SAIU DA JAULA O MONSTRO {} - e ce passou {} e {}'.format(ctx.author, nomeExercicio, repeticoesSeries))
    if len(args) == 0:
        await ctx.send('Zero argumentos recebidos, esperado pelo menos 1.')
    elif len(args) == 1:
        exibePlacarExercicio(args)
    elif len(args) == 2:
        registraExercicio(ctx.author, args)
    else:
        await ctx.send('Argumento inválido.')

def registraExercicio(author, args):
    repeticoesSeries = args[1].split(":")
    registroExercicio = Exercicio(args[0], repeticoesSeries[0], repeticoesSeries[1], author)
    scoreboard.add(registroExercicio)

def exibePlacarExercicio(args):
    scoreboard.status(args[0])

bot.run(TOKEN)