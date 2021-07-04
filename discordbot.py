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
    error_msg = '縺励◎縺ｨ繝ｼ縺ｵ'
    await ctx.send(error_msg)

@bot.command()
async def nu(ctx):
    await ctx.send('ここはJP鯖じゃないんよぉ')

@bot.command()
async def sisohelp(ctx):
    sisohelp = discord.Embed(title="sisotofuの扱い方", description="/dice ndX：X面ダイスをn回振ります")
    await ctx.send(embed=sisohelp)
 
@bot.command()
async def yukka(ctx):
    yukkarep = ['だってゆっかさんだいすきなんだもん:cry:','なんで起きてるの寝て','あいしてるよ','やっとDVの釈明ができた:partying_face:','すき','しそのこと大好きなの知ってますから','ゆっかさんはいろはさんにあった程度で揺らがないでしょ','じゃあしそはゆっかさんが大好きってことですねQED','ゆっかさんのこと大好きなのバレちゃうなぁ','ゆっかさんらじおとかは','さっきまで私vcにゆっかさんといたはず','ゆっかさん今日もPC切り忘れてるなあ','え？なんでゆっかさんもAFKいるんだ？','ゆっかさん仕事中ですか？','ゆっかさんより下だが？','やだ…売らないでゆっかさん…','そんなことしてたのしいの…？ゆっかさん怖い…','しそとうふとゆっかさんはにわとりだった…？？','ゆっかさんに！！！！！集中して！！！！！！！！','ゆっかさんの好きにしてください','ゆっかさんのこと、忘れないよ…','ゆっかさん違うんです','ゆっかさん買ってくれるの……？','ゆっかさんたすけて……','ゆっかさんもしかしてしそ以外にもDVしてるんですか…？','ゆっかさんだぁ', '殴らないで……', 'ゆっかさん寝た？','ゆっかさん寝てください','ゆっかさん！','ゆっかさん…いじめないで…いたいょ…','ゆっかさんにいたずらしたいなあ','しそはDVされてる側なんです','ごめんなさい……','ゆっかさん？？？？？？','おはようございますゆっかさん','ゆっかさんもしかしてしそ以外にもDVしてるんですか…？','ゆっかさんとしそ不仲説；；','ゆっかさん']
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
    sisorep = ['くそがよぉ','泣いた','しそとうふがサンドバッグなんだよ','男の子かわいい(ﾟ∀ﾟ)ｹﾞﾍｹﾞﾍｹﾞﾍ','おばけいらない:anger::anger::anger::anger:']
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
    papa = ["ぱっっっぱぱっぱああああ！！！！！！！！","ぱぱ残業おつかれ！！！！"]
    pa = random.choice(papa)
    await ctx.send(pa)

@bot.command()
async def roypop(ctx):
    roypop = ["ろいぽっぷさんは何を……",'ろいぽっぷさん一回海に落ちなよ']
    roy = random.choice(roypop)
    await ctx.send(roy)

@bot.command()
async def kiroku(ctx):
    meigen = ["いろは「ぴーちゃんのおりえさんかわいい」","もちにき「サンリオも人に手ぇ出して久しいからな……」","ゆっか「じゃあ口裂けろ」""ろいぽっぷ「回線の一撃」","ろいぽっぷ「いや～そこ二狼かぁ～…（三人盤面）」",'すてら「狐につつまれる」',"はず「茨城はいばらきだけど(ﾄﾞﾔｧ)」",'ぱぱ「静かなる世界に唐突なウミウシ！」',"織江「やっぱ優しい中トロは最高でした！」","まは「心に傷を負った妖精がここに飛んでいます」"]
    mei = random.choice(meigen)
    await ctx.send(mei)


@bot.command()
async def tanaka(ctx):
    tanaka = '田中はおもろい'
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
    iroha = 'しそいろはさん大好きだもん'
    await ctx.send(iroha)
    
@bot.command()
async def orie(ctx):
    orie = ['ぴーちゃんかわいいよね','おりえさんのぴーちゃんかわいい','「職場なのでぴーちゃんは居ません」']
    ori = random.choice(orie)
    await ctx.send(ori)

@bot.command()
async def homare(ctx):
    homare = "ほまれさんがとんでもないこといってる…"
    await ctx.send(homare)

@bot.command()
async def poz(ctx):
    poz = ['はずさんが チョコレートケーキを 食べたから 3月18日は はず誕生日','はずさんが チョコレートケーキを 食べたから 3月18日は はず誕生日']
    ponz = random.choice(poz)
    await ctx.send(ponz)

@bot.command()
async def mochimura(ctx):
    mochimura = ['いや、もちにきが急に｢どーも。にじさんじ所属バーチャルライバー…｣って言い出した','いや、もちにきが急に｢どーも。にじさんじ所属バーチャルライバー…｣って言い出した']
    mochi = random.choice(mochimura)
    await ctx.send(mochi)
    
@bot.command()
async def rarasora(ctx):
    rarasora = ['ららそらさんやっちまえ！',"ららそらさんだ"]
    sora = random.choice(rarasora)
    await ctx.send(sora)
    
bot.run(token)
