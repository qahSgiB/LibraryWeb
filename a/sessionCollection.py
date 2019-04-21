from a.mongo import databases
from a.usersCollection import usersCollection



sessionsCollection = databases['sessions']



def getSessionUser(sid):
    session = sessionsCollection.find_one({'sid': sid})
    userId = session['user']

    if userId == -1:
        return None
    else:
        user = usersCollection.find_one({'id': userId})
        return user

def addSession(session):
    sessionsCollection.insert_one(session)

def setSessionUser(sid, newUser):
    sessionsCollection.update_one({'sid': sid}, {'$set': {'user': newUser}})