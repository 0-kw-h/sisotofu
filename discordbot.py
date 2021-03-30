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

async def on_message(message):
    # 開始ワード
    if message.content.startswith('dice'):
        # 送り主がBotではないか
        if client.user != message.author:
            info = parse('dice {}d{} {}', message.content)
            if info:
                if info[1].isdecimal() and info[0].isdecimal():
                    dice_num = int(info[0])
                    dice_size = int(info[1])
                    key = info[2]
                    # メッセージを書きます
                    m = message.author.name + ' '
                    if key == '一時的狂気':
                        m = temp_madness()
                    elif key == '不定の狂気':
                        m = ind_madness()
                    elif key == 'dice':
                        m = simple_dice(dice_size, dice_num)
                    else:
                        chara = get_charactor(str(message.author))
                        msg, result = judge(chara, key, dice_size, dice_num)
                        m += msg
                        if result:
                            d = damage(chara, key)
                        else:
                            d = None
                        if d is not None:
                            m += '\nダメージ: ' + str(np.sum(d)) + ' = ' + str(d)
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await client.send_message(message.channel, m)

bot.run(token)
