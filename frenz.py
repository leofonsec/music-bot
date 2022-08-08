from ast import alias
import discord
from discord.ext import commands
import os

class frenz_cog(commands.Cog):
    @commands.command(name="id", help="comando para exibir seu id no discord")
    async def id(self, ctx):
        await ctx.send(ctx.author)

    @commands.command(name="udsu", aliases=["u"], help="comando para nosso imortal")
    async def udsu(self, ctx):
        await ctx.send("Udson Bolas, nosso IMORTAL!")

    @commands.command()
    async def adm(self, ctx):
        await ctx.send("O SUPRASSUMO DA ORDEM, BRUNELO!")

    @commands.command()
    async def thati(self, ctx):
        await ctx.send("Vc procura pela Thatiana A TROLL?")