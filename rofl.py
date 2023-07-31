import asyncio
import discord
import random
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/',
                   intents=intents,
                   help_command=None)

@bot.event
async def on_ready():
    print(f'[BOT] Успешно запущен\nLogged in as {bot.user.name}')
    print('Logged in as', bot.user.name)
    print('Создатель бота - kekyoko')

@bot.command()
async def kyoko(ctx, member: discord.Member):
    if ctx.author.guild_permissions.administrator:

        voice_channels = ctx.guild.voice_channels

        await member.move_to(random.choice(voice_channels))

        await member.edit(mute=True)

        await asyncio.sleep(10)

        await member.edit(mute=False)
    else:
        await ctx.send("У вас нет прав администратора для выполнения этой команды.")

bot.run(config.TOKEN)

#Создатель бота KeKyoko (git - github.com/kekyoko)
# nipaaaaaa