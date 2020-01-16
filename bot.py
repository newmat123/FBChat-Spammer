from fbchat import Client
from fbchat.models import *
import time

#pip install fbchat is needed for this project

#finds and opens my profile
def findMe():
    global client
    print("your phone number:")
    Number = input("")
    print("your password for facebook:")
    Password = input("")

    print("looking for user...")
    client = Client(int(Number), Password)

    print("Own id: {}".format(client.uid))
    findUser()


#finds the the target
def findUser():
    global user

    print("who do you want to target?")
    target = input("")

    print("looking for target...")
    users = client.searchForUsers(target)
    user = users[0]

    print("User's name: {}".format(user.name))
    print("User's profile picture URL: {}".format(user.photo))
    definMessege()


#defins what messeges to send
def definMessege():
    global text

    print("type the meseges you want to spam:")
    text = Message(input())
    sendIt()


#sends it
def sendIt():
    print("how meany times do you want to send it?:")
    x = input("")

    print("spaming...")

    i = 0
    while i < int(x):
        client.send(text, thread_id=user.uid, thread_type=ThreadType.USER)
        i += 1
        time.sleep(0.1)

    print("done")
    print("")
    print("")
    print("")
    findUser()



#start
if __name__ == '__main__':
    findMe()
