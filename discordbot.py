from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    await ctx.send(呼びましたか？)

@bot.command()
async def sisotofu(ctx):
    await ctx.send('くそがよぉ')


@bot.command()
async def DV(ctx):
    await ctx.send('殴らないで……')


bot.run(token)
