from ast import alias
from unicodedata import name
import discord
from discord.ext import commands
import os
from youtube_dl import YoutubeDL
from music import music_cog
from frenz import frenz_cog
import ffmpeg

bot = commands.Bot(command_prefix='.')

bot.add_cog(frenz_cog(bot))
bot.add_cog(music_cog(bot))

bot.run('MTAwNTYxMjE4NDkyOTMyMDk5MA.GzIJK3.y9ZewjyeyS2l6Rlvne4UhwKBacYsmUfW8U9efg')