from a.mongo import usersCollection



def getLastUserId():
    lastUserId = usersCollection.find({}, {'id': 1, '_id': 0}).sort('id', -1).limit(1)[0]['id']
    return lastUserId

def addUser(newUser):
    usersCollection.insert_one(newUser)