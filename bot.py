import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(">>Bot is on <<")

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}ms')

bot.run('你的機器人Token')
