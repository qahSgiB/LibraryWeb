from bson.int64 import Int64 as mongoInt64

from pyPage.settings.view import getDefaultSettings

from a.usersCollection import getLastUserId, addUser



settings = getDefaultSettings()
settings['isRedirect'] = True



def view(getData, postData, cookies):
    newUser = {
        'id': mongoInt64(getLastUserId()+1),
        'first_name': postData['first_name'],
        'last_name': postData['last_name'],
        'mail': postData['mail'],
        'isic': postData['isic'],
        'password': postData['password'],
    }

    addUser(newUser)

    return '/', []