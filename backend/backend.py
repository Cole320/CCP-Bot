import json
import config

with open(config.bad_words_list, 'r') as badWordsJson:
    badWords = json.loads(badWordsJson.read())

with open(config.good_words_list, 'r') as goodWordsJson:
    goodWords = json.loads(goodWordsJson.read())


# Find a better way of doing this - nicole <3
def isGood(message):
    for word in goodWords:
        if word.lower() in message.lower():
            print('test')
            return goodWords[word]

    return False


def isBad(message):
    for word in badWords:
        if word.lower() in message.lower():
            return badWords[word]

    return False
