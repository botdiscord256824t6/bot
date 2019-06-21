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

    # give info about you here
    embed.add_field(name="Author", value="LeMIT")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discord.gg/")

    await ctx.send(embed=embed)

# bot.remove_command('help')


# @bot.command()
# async def help(ctx):
    # embed = discord.Embed(title=botname, description="A" +
    # botname + "." + " List of commands are:", color=0xeee657)

    # embed.add_field(
    # name="$plus X Y", value="Gives the addition of **X** and **Y**", inline=False)
    # embed.add_field(name="$umnozit X Y",
    # value="Gives the multiplication of **X** and **Y**", inline=False)
    # embed.add_field(
    # name="$greet", value="Gives a nice greet message", inline=False)
    # embed.add_field(
    # name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    # embed.add_field(
    # name="$info", value="Gives a little info about the bot", inline=False)
    #embed.add_field(name="$help", value="Gives this message", inline=False)
    # await ctx.send(embed=embed)


# @bot.command()
# async def modhelp(ctx):
    # embed = discord.Embed(
    # title=botname, description='List of moderator command are:', color=0xeee657)
    #embed.add_field(name="%kick", value="Kick user", inline=False)
    #embed.add_field(name="%ban", value="Ban user", inline=False)
    #embed.add_field(name="%mute", value="Mute user", inline=False)
    # await ctx.send(embed=embed)

bot.run(token)
