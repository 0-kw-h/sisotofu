from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = 'このBOTはしそとうふさんの善意により運営されています。感謝を欠かすことの無いよう、常々意識をお願いします。'
    await ctx.send(error_msg)

@bot.command()
async def yukka(ctx):
    yukkarep = ['ゆっかさんだぁ', '殴らないで……', 'ゆっかさん寝た？','ゆっかさん寝てください','ゆっかさん！','ゆっかさん…いじめないで…いたいょ…','ゆっかさんにいたずらしたいなあ','しそはDVされてる側なんです','ごめんなさい……','ゆっかさん？？？？？？','おはようございますゆっかさん','ゆっかさんもしかしてしそ以外にもDVしてるんですか…？','ゆっかさんとしそ不仲説；；']
    ya = random.choice(yukkarep)
    await ctx.send(ya)

@bot.command()
async def dice(ctx):
    await ctx.send(random.randint(0,100))

@bot.command()
async def sisotofu(ctx):
    sisorep = ['くそがよぉ','泣いた','はらたつ']
    sa = random.choice(sisorep)
    await ctx.send(sa)

@bot.command()
async def stella(ctx):
    s = "すてら"
    await ctx.send(s)

@bot.command()
async def maha(ctx):
    m = "まはさんなら大丈夫ですよ"
    await ctx.send(m)

@bot.command()
async def yankeee(ctx):
    yankeee = "はらたつ"
    await ctx.send(yankeee)

@bot.command()
async def sigure(ctx):
    si = "れこそそさんだ"
    await ctx.send(si)

@bot.command()
async def recososo(ctx):
    re = "しぐれかー"
    await ctx.send(re)

bot.run(token)
