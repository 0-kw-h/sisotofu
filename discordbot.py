
import os
import random
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/sisotofu':
        await message.channel.send('くそがよぉ')
        
@bot.command()
async def dice(ctx):
    await ctx.send(random.randint(0,100))
    
bot.run(token)
