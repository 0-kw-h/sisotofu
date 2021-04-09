import discord
from discord.ext import commands
import os
import re
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
async def nu(ctx):
    await ctx.send('ここはJP鯖じゃないんよぉ')


@bot.command()
async def sleep(ctx,afk):
    admin = str(afk)
    await ctx.send(afk + 'おやすみなさい')
    
@bot.command()
async def sisohelp(ctx):
    sisohelp = discord.Embed(title="sisotofuの扱い方", description="/dice ndX：X面ダイスをn回振ります")
    await ctx.send(embed=sisohelp)
 
@bot.command()
async def yukka(ctx):
    yukkarep = ['ゆっかさんらじおとかは','さっきまで私vcにゆっかさんといたはず','ゆっかさん今日もPC切り忘れてるなあ','え？なんでゆっかさんもAFKいるんだ？','ゆっかさん仕事中ですか？','ゆっかさんより下だが？','やだ…売らないでゆっかさん…','そんなことしてたのしいの…？ゆっかさん怖い…','しそとうふとゆっかさんはにわとりだった…？？','ゆっかさんに！！！！！集中して！！！！！！！！','ゆっかさんの好きにしてください','ゆっかさんのこと、忘れないよ…','ゆっかさん違うんです','ゆっかさん買ってくれるの……？','ゆっかさんたすけて……','ゆっかさんもしかしてしそ以外にもDVしてるんですか…？','ゆっかさんだぁ', '殴らないで……', 'ゆっかさん寝た？','ゆっかさん寝てください','ゆっかさん！','ゆっかさん…いじめないで…いたいょ…','ゆっかさんにいたずらしたいなあ','しそはDVされてる側なんです','ごめんなさい……','ゆっかさん？？？？？？','おはようございますゆっかさん','ゆっかさんもしかしてしそ以外にもDVしてるんですか…？','ゆっかさんとしそ不仲説；；','ゆっかさん']
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
    sisorep = ['くそがよぉ','泣いた','お腹すいた……','非正規ルートおねぇさんでーす','しそは数学のおねぇさんなので']
    sa = random.choice(sisorep)
    await ctx.send(sa)

@bot.command()
async def stella(ctx):
    stella = ['すてらー！！！！','いっそのこと、いかやきにしよう']
    ste = random.choice(stella)
    await ctx.send(ste)

@bot.command()
async def maha(ctx):
    m = "まはさんいないのめずらしいな"
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
    re = ['時雨に傘で殴られかけました','しぐれかー']
    recososo = random.choice(re)
    await ctx.send(recososo)

@bot.command()
async def papa(ctx):
    pa = "ぱっっっぱぱっぱああああ！！！！！！！！"
    await ctx.send(pa)

@bot.command()
async def roypop(ctx):
    roypop = ["ろいぽっぷさんは何を……",'ろいぽっぷさん一回海に落ちなよ']
    roy = random.choice(roypop)
    await ctx.send(roy)

@bot.command()
async def tanaka(ctx):
    tanaka = '田中台パンしてる？？？？？？？？？？'
    await ctx.send(tanaka)

@bot.command()
async def haz(ctx):
    haz = 'はずさんがいっぱいらじおすれば無問題ですよ'
    await ctx.send(haz)
    
@bot.command()
async def zukkai(ctx):
    zukkai = 'ずっかいシェフに来てもらいましょう'
    await ctx.send(zukkai)

@bot.command()
async def iroha(ctx):
    iroha = 'いろはさんはまじでやばい'
    await ctx.send(iroha)
    
@bot.command()
async def orie(ctx):
    orie = 'おりえさんのぴーちゃんかわいい'
    await ctx.send(orie)

@bot.command()
async def homare(ctx):
    homare = "ほまれさんがとんでもないこといってる…"
    await ctx.send(homare)
    
bot.run(token)
