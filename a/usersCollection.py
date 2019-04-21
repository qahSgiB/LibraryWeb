from a.mongo import databases



usersCollection = databases['users']



def getLastUserId():
    lastUserId = usersCollection.find({}, {'id': 1, '_id': 0}).sort('id', -1).limit(1)[0]['id']
    return lastUserId

def addUser(newUser):
    usersCollection.insert_one(newUser)

def tryLogin(mail, password):
    user = usersCollection.find_one({'mail': mail})

    loginSuccesful = True
    details = {}

    if user == None:
        loginSuccesful = False
        details['errorMessage'] = 'user_not_found'
    else:
        if user['password'] != password:
            loginSuccesful = False
            details['errorMessage'] = 'wrong_password'

    if loginSuccesful:
        details['user'] = user

    return loginSuccesful, details