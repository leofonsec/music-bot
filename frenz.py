from ast import alias
import discord
from discord.ext import commands
import os

class frenz_cog(commands.Cog):
    @commands.command(name="id", help="Comando para exibir seu id no discord")
    async def id(self, ctx):
        await ctx.send(ctx.author)

    @commands.command(name="udsu", aliases=["u"], help="Comando para nosso imortal")
    async def udsu(self, ctx):
        await ctx.send("Udson Bolas, nosso IMORTAL!")

    @commands.command(help="Comando para nosso saudoso ADM")
    async def adm(self, ctx):
        await ctx.send("O SUPRASSUMO DA ORDEM, BRUNELO!")

    @commands.command(help="Comando para a mais troll do mundo")
    async def thati(self, ctx):
        await ctx.send("Vc procura pela Thatiana A TROLL?")
    
    @commands.command(help="comando teste pro habila")
    async def habila(self, ctx):
        await ctx.send("Teste pro meu mano Habila")