import discord
from discord.ext import commands

import config
from database import database
from backend import backend

bot = commands.Bot(command_prefix=config.prefix, activity=discord.Game(name=config.custom_status))

print('Initializing Bot With Prefix: ' + config.prefix)
database.initDB()


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def addSC(message):
    database.addSC(message.author.id, 100)
    print(message.author.id)
    print(message.author.id)
    await message.send("pong")


@bot.command()
async def fetchSC(message):
    await message.send(database.fetchSC(message.author.id))


@bot.event
async def on_message(message):
    is_bad = backend.isBad(message.content)
    is_good = backend.isGood(message.content)

    if is_bad:
        database.subtractSC(message.author.id, is_bad)
        database.badWord(message.author.id)

    if is_good:
        database.addSC(message.author.id, is_good)
        database.goodWord(message.author.id)

    database.addUser(message.author.id, message.author)

    await bot.process_commands(message)

bot.run(config.token)
