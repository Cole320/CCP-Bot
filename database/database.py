import config
from tinydb import TinyDB, Query

db = TinyDB(config.database_path)
User = Query()
db = db.table('Users')


def initDB():
    # addUser('373808586150772738', 'Coal')
    # addUser('373808586150772738', 'Coal2')
    pass


def getUserInfo(user_id):
    # If the list returned by the database of matching users is null, add a user
    try:
        cur_user = db.search(User.userID == int(user_id))[0]

    except IndexError:
        return False


def addUser(user_id):
    # If the list returned by the database of matching users is null, add a user
    try:
        db.search(User.userID == int(user_id))[0]

    except IndexError:
        db.insert({'userID': user_id,
                   'canSpeak': True,
                   'socialCredit': config.starting_social_credit,
                   'merits': 0,
                   'demerits': 0
                   })


# TODO: Make this better <3
def subtractSC(user_id, amount):
    cur_user = db.search(User.userID == int(user_id))[0]

    if cur_user['socialCredit'] - amount < 0:
        db.update({'socialCredit': 0}, User.userID == int(user_id))
    else:
        db.update({'socialCredit': cur_user['socialCredit'] - amount}, User.userID == int(user_id))


def addSC(user_id, amount):
    cur_user = db.search(User.userID == int(user_id))[0]
    db.update({'socialCredit': cur_user['socialCredit'] + amount}, User.userID == int(user_id))


def goodWord(user_id):
    cur_user = db.search(User.userID == int(user_id))[0]
    db.update({'merits': cur_user['merits'] + 1}, User.userID == int(user_id))


def badWord(user_id):
    cur_user = db.search(User.userID == int(user_id))[0]
    db.update({'demerits': cur_user['demerits'] + 1}, User.userID == int(user_id))


def fetchSC(user_id):
    cur_user = db.search(User.userID == int(user_id))[0]
    return cur_user['socialCredit']


def fetchMerits(user_id):
    cur_user = db.search(User.userID == int(user_id))[0]
    return cur_user['merits']


def fetchDemerits(user_id):
    cur_user = db.search(User.userID == int(user_id))[0]
    return cur_user['demerits']
