import config
from tinydb import TinyDB, Query, Storage

db = TinyDB(config.database_path)
User = Query()
db = db.table('Users')


def initDB():
    addUser('373808586150772738', 'Coal')
    addUser('373808586150772738', 'Coal2')


def addUser(user_id, name):
    try:
        db.search(User.userID == str(user_id))[0]

    except IndexError:
        db.insert({'userID': user_id,
                   'name': name,
                   'canSpeak': True,
                   'socialCredit': config.starting_social_credit,
                   'goodWords': 0,
                   'badWords': 0
                   })


def subtractSC(user_id, amount):
    cur_user = db.search(User.userID == str(user_id))[0]

    if cur_user['socialCredit'] - amount < 0:
        db.update({'socialCredit': 0}, User.userID == str(user_id))
    else:
        db.update({'socialCredit': cur_user['socialCredit'] - amount}, User.userID == str(user_id))


def addSC(user_id, amount):
    cur_user = db.search(User.userID == str(user_id))[0]
    db.update({'socialCredit': cur_user['socialCredit'] + amount}, User.userID == str(user_id))


def goodWord(user_id):
    cur_user = db.search(User.userID == str(user_id))[0]
    db.update({'goodWords': cur_user['goodWords'] + 1}, User.userID == str(user_id))


def badWord(user_id):
    cur_user = db.search(User.userID == str(user_id))[0]
    db.update({'badWords': cur_user['badWords'] + 1}, User.userID == str(user_id))


def fetchSC(user_id):
    print(user_id)
    cur_user = db.search(User.userID == str(user_id))[0]
    return cur_user['socialCredit']
