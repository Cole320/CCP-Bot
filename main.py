import discord
from discord.ext import commands

import config
from database import database
from backend import backend

bot = commands.Bot(command_prefix=config.prefix, activity=discord.Game(name=config.custom_status))

print('Initializing Bot With Prefix: ' + config.prefix)
database.initDB()


@bot.command(brief='Add SC to a mentioned user')
async def addSC(message, amount):
    if message.message.mentions[0]:
        user = message.message.mentions[0]
    else:
        user = message.author
        database.addUser(user.id)

    database.addSC(user.id, int(amount))
    await message.send(
        'Social Credit Manually Increased for User: ' + str(message.author) + ' by ' + amount + ' points.')


@bot.command(brief='Remove SC from a mentioned user')
async def subtractSC(message, amount):
    if message.message.mentions[0]:
        user = message.message.mentions[0]
    else:
        user = message.author
        database.addUser(user.id)

    database.subtractSC(user.id, int(amount))
    await message.send(
        'Social Credit Manually Decreased for User: ' + str(message.author) + ' by ' + amount + ' points.')


@bot.command(brief='Retrieve and display SC for a mentioned user')
async def fetchSC(message):
    try:
        if message.message.mentions:
            embed = backend.fetchSCEmbed(message.message.mentions[0])
        else:
            embed = backend.fetchSCEmbed(message.author)


    except IndexError:
        database.addUser(message.message.mentions[0].id)
        embed = backend.fetchSCEmbed(message.message.mentions[0])

    await message.send(embed=embed)


@bot.event
async def on_message(message):
    demerit = backend.isBad(message.content)
    merit = backend.isGood(message.content)

    if demerit:
        database.subtractSC(message.author.id, demerit)
        database.badWord(message.author.id)
        await message.add_reaction('❌')

    if merit:
        database.addSC(message.author.id, merit)
        database.goodWord(message.author.id)
        await message.add_reaction('✅')

    database.addUser(message.author.id)

    await bot.process_commands(message)


bot.run(config.token)
