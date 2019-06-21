import discord
from discord.ext import commands
import asyncio
import youtube_dl
import requests as rq
from discord import opus


token = ',,'
prefix = '%'
botname = ',,'

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print('Бот был запущен с параметрами:')
    print('Имя бота:' + bot.user.name + botname)
    print('ID бота:' + str(bot.user.id))
    print('------')


@bot.command()
async def plus(ctx, a: int, b: int):
    await ctx.send(a + b)


@bot.command()
async def umnozit(ctx, a: int, b: int):
    await ctx.send(a * b)


@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send("__**Successfully User" + member + "Has Been Kicked!**__")


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send("__**Successfully User" + member + " Has Been Baned!**__")


@bot.command()
@commands.has_permissions(manage_roles=True, ban_members=True)
async def mute(ctx, member: discord.Member):
    role = await discord.utils.get(ctx.guild.roles, name='Muted')


@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Test bot", description="Nicest bot there is ever.", color=0xeee657)
    embed.add_field(name="Author", value="LeMIT")
    embed.add_field(name="Guild count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite", value="https://discord.gg/5CHCJk2")
    await ctx.send(embed=embed)

bot.run(token)
