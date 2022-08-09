from ast import alias
from distutils.log import info
from http.server import executable
from nturl2path import url2pathname
from pickle import FALSE
import discord
from discord.ext import commands
import youtube_dl
from youtube_dl import YoutubeDL
import ffmpeg

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
    
    async def teste(self, ctx):
        vchannel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await vchannel.connect()
        else:
            await ctx.voice_client.move_to(vchannel)

    
    @commands.command(aliases = ['j'], help = "Comando pro Vagnao conectar.")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Entra num canal ae chupinga")
        if self.is_playing == False:
            await self.teste(ctx)
    
    @commands.command(aliases = ['d', 'leave', 'l'], help = "Comando pro Vagnao desconectar.")
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(aliases = ['p'], help = "Comando pro Vagnao tocar seu som!")
    async def play(self, ctx, url):
        if self.is_playing == False:
            await self.teste(ctx)
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        song = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info ['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            song.play(source)
    
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.voice_client.is_paused()
        await ctx.send("Pausudo... Digo, pausado")
    
    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.voice_client.is_playing()
        await ctx.send("Voltando")