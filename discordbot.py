from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send('どうして……')

@bot.command()
async def sisotofu(ctx):
    await ctx.send('くそがよぉ')

@bot.command()
async def DV(ctx):
    await ctx.send('殴らないで……')

@bot.command()
async def yukka(ctx):
    await ctx.send('ゆっかさんだー')


@bot.command()
async def 1d100:
    b = random.randint(0,100)
    await ctx.send(b)


bot.run(token)
