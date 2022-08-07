import discord
from discord.ext import commands
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

bot = commands.Bot(command_prefix='.')

@bot.command()
async def info(ctx):
    await ctx.send(ctx.author)

client = MyClient()
client.run('MTAwNTYxMjE4NDkyOTMyMDk5MA.GzIJK3.y9ZewjyeyS2l6Rlvne4UhwKBacYsmUfW8U9efg')