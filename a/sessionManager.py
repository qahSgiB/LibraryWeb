import os
import time
import hashlib
from bson.int64 import Int64 as mongoInt64

from pyPage.Cookie import Cookie

from a.sessionCollection import addSession, setSessionUser, getSessionUser



def generateSessionId():
    rndA = os.urandom(64)
    rndB = os.urandom(64)
    timeStr = bytes(str(time.time()), 'UTF-8')

    data = rndA+timeStr+rndB
    sid = hashlib.sha256(data).hexdigest()

    return sid

def generateSessionCookie():
    cookie = Cookie('sid', generateSessionId())

    return cookie

def checkSession(cookies):
    sessionCookie = None

    for cookie in cookies:
        if cookie.name == 'sid':
            sessionCookie = cookie
            break

    if sessionCookie == None:
        sessionCookie = generateSessionCookie()

        session = {
            'sid': sessionCookie.value,
            'user': mongoInt64(-1),
        }
        addSession(session)

    sessionCookie.setExpirationTimeY(1)
    sessionCookie.setPath('/')

    return sessionCookie

def checkSessionDecorator(viewF):
    def newViewF(getData, postData, cookies):
        sessionCookie = checkSession(cookies)

        response, cookies = viewF(getData, postData, cookies, sessionCookie)
        cookies.append(sessionCookie)

        return response, cookies

    return newViewF

def login(sid, userId):
    setSessionUser(sid, userId)

def logout(sid):
    setSessionUser(sid, -1)