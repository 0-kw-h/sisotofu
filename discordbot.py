import discord
import asyncio
import os
import random
import botFunction.functions as f
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/sisotofu':
        await message.channel.send('くそがよぉ')
        
@bot.command()
async def dice(ctx):
    await ctx.send(random.randint(0,100))
    
bot.run(token)
