from connection import db

Emails = db['emails']


def findEmail(record):
    return Emails.find_one(record)


def createEmail(record):
    res = findEmail(record)
    if res:
        return res
    res = Emails.insert_one(record)
    id = res.inserted_id
    return findEmail({'_id': id})
