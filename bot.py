from fbchat import Client
from fbchat.models import *


#defins what messeges to send
def definMessege():
    global text

    text = Message(input())
    sendIt()


#finds and opens my profile
def findMe():
    global client

    client = Client(xxxxxx, "xxxxxx")
    print("Own id: {}".format(client.uid))
    findUser()


#finds the the target
def findUser():
    global user

    users = client.searchForUsers('nicklas')
    user = users[0]

    print("User's ID: {}".format(user.uid))
    print("User's name: {}".format(user.name))
    print("User's profile picture URL: {}".format(user.photo))
    print("User's main URL: {}".format(user.url))
    definMessege()


#sends it
def sendIt():
    client.send(text, thread_id=user.uid, thread_type=ThreadType.USER)
    logoutBot()


#logs out
def logoutBot():
    client.logout()


#start
if __name__ == '__main__':
    findMe()
