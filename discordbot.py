import discord
from discord.ext import commands
import os
import re
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command() 
async def siso(ctx):
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect() 

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = 'このBOTはしそとうふさんの善意により運営されています。感謝を欠かすことの無いよう、常々意識をお願いします。'
    await ctx.send(error_msg)

@bot.command()
async def nu(ctx):
    await ctx.send('ここはJP鯖じゃないんよぉ')

@bot.command()
async def sleep(ctx,message):
    repo = [member.id for member in message.mentions]
    await ctx.send(message)
    await ctx.send(repo)

    
@bot.command()
async def yukka(ctx):
    yukkarep = ['ゆっかさんの好きにしてください','ゆっかさんのこと、忘れないよ…','ゆっかさん違うんです','ゆっかさん買ってくれるの……？','ゆっかさんたすけて……','ゆっかさんもしかしてしそ以外にもDVしてるんですか…？','ゆっかさんだぁ', '殴らないで……', 'ゆっかさん寝た？','ゆっかさん寝てください','ゆっかさん！','ゆっかさん…いじめないで…いたいょ…','ゆっかさんにいたずらしたいなあ','しそはDVされてる側なんです','ごめんなさい……','ゆっかさん？？？？？？','おはようございますゆっかさん','ゆっかさんもしかしてしそ以外にもDVしてるんですか…？','ゆっかさんとしそ不仲説；；']
    ya = random.choice(yukkarep)
    await ctx.send(ya)

@bot.command()
async def dice(ctx,diceinp):
    dicenum = diceinp.split('d')
    ans = []
    a = int(dicenum[0])
    b = int(dicenum[1])
    for i in range(a):
      ans.append(random.randint(1,b))
    diceres = sum(ans) 
    await ctx.send(diceres)
    await ctx.send(ans)
        
@bot.command()
async def sisotofu(ctx):
    sisorep = ['くそがよぉ','泣いた','お腹すいた……']
    sa = random.choice(sisorep)
    await ctx.send(sa)

@bot.command()
async def stella(ctx):
    s = "すてらー！！！！"
    await ctx.send(s)

@bot.command()
async def maha(ctx):
    m = "まはさん"
    await ctx.send(m)

@bot.command()
async def yankee(ctx):
    yankeee = "はらたつ"
    await ctx.send(yankeee)

@bot.command()
async def shigure(ctx):
    si = "れこそそさんだ"
    await ctx.send(si)

@bot.command()
async def recososo(ctx):
    re = "しぐれかー"
    await ctx.send(re)

@bot.command()
async def papa(ctx):
    pa = "ぱっっっぱぱっぱああああ！！！！！！！！"
    await ctx.send(pa)

@bot.command()
async def roypop(ctx):
    roy = "ろいぽっぷさんは何を……"
    await ctx.send(roy)

@bot.command()
async def tanaka(ctx):
    tanaka = '田中台パンしてる？？？？？？？？？？'
    await ctx.send(tanaka)

@bot.command()
async def haz(ctx):
    haz = 'はずさんが チョコレートケーキを 食べたから 3月18日は はず誕生日'
    await ctx.send(haz)

bot.run(token)

