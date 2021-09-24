import json
import config
import discord

from database import database

with open(config.bad_words_list, 'r') as badWordsJson:
    badWords = json.loads(badWordsJson.read())

with open(config.good_words_list, 'r') as goodWordsJson:
    goodWords = json.loads(goodWordsJson.read())


# Find a better way of doing this - nicole <3
def isGood(message):
    for word in goodWords:
        if word.lower() in message.lower():
            return goodWords[word]

    return False


def isBad(message):
    for word in badWords:
        if word.lower() in message.lower():
            return badWords[word]

    return False


def fetchSCEmbed(author):
    embed = discord.Embed(colour=discord.Colour(0xEE1620), url='https://github.com/Cole320/CCP-Bot',
                          description='社會信用檢查')

    embed.set_thumbnail(
        url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/43'
            '/Flag_of_the_Communist_Party_of_the_Philippines_%28alternative_II%29.svg/800px'
            '-Flag_of_the_Communist_Party_of_the_Philippines_%28alternative_II%29.svg.png'
    )

    embed.set_author(name=author.name,
                     url='https://github.com/Cole320/CCP-Bot',
                     icon_url=author.avatar_url
                     )

    embed.add_field(name='Social Credit:', value=str(database.fetchSC(author.id)), inline=False)
    embed.add_field(name='Merits:', value=database.fetchMerits(author.id), inline=False)
    embed.add_field(name='Demerits:', value=database.fetchDemerits(author.id), inline=False)
    embed.set_footer(text='<' + ('-' * 5) + 'Always Remember: Glory to the CCP!' + ('-' * 5) + '>')

    return embed
