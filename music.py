from ast import alias
from unicodedata import name
import discord
from discord.ext import commands
import os
from youtube_dl import YoutubeDL
#from ytf import music_cog

bot = commands.Bot(command_prefix='.')

@bot.command(name="id", help="comando para exibir seu id no discord")
async def id(ctx):
    await ctx.send(ctx.author)

@bot.command(name="udsu", aliases=["u"], help="comando para nosso imortal")
async def udsu(ctx):
    await ctx.send("Udson Bolas, nosso IMORTAL!")

@bot.command()
async def adm(ctx):
    await ctx.send("O SUPRASSUMO DA ORDEM, BRUNELO!")

@bot.command()
async def thati(ctx):
    await ctx.send("Vc procura pela Thatiana A TROLL?")

bot.run('MTAwNTYxMjE4NDkyOTMyMDk5MA.GzIJK3.y9ZewjyeyS2l6Rlvne4UhwKBacYsmUfW8U9efg')