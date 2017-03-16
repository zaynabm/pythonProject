
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import json
from tornado.escape import json_encode
from pymongo import MongoClient
from handlers.index import IndexHandler


clients = []    #********** List of clients Info
onlineFriends=[] #********** List of Online Friends name
offlineFriends=[]
sender=[]
mes=[]

client = MongoClient('localhost', 27018)
db = client.chatRR  # name of database
collection=db['users'] # name of collection
groupCollection=db['groups']

#########################################################################
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("SOCKT Connection Started from ")

    def on_message(self, message):  #{"msgType":'Notify',"loginName":loginName,"content":msgToSend,"chatRoom":chatRoom,"roomType":roomType};
        msg=json.loads(message)
        dumpMessage=json.dumps(msg)

        msgType=msg['msgType']
        senderName=msg['loginName']
        roomType=msg['roomType']
        currentChatRoom=msg['chatRoom']  #********** current Chat Room
        msgContent=msg['content']

        if(msgType=='Notify'):
            print("Type of msgg->  Notify")
            allUsersObj=db.users.find({},{"_id":0,"name":1})  # all users from DB
            offlineFriends=[]
            for val in allUsersObj:
                offlineFriends.append(val['name'])
            print("offfffffffffff",offlineFriends)
            client={'name':senderName,'id':self,'currentRoom':currentChatRoom,'roomType':roomType}
            print("new client connected: ",client)
            clients.append(client)
            onlineFriends.append(senderName)
            offlineFriends.remove(senderName)

            strListOfOnlineFriends=' '.join(onlineFriends)
            strListOfOfflineFriends=' '.join(offlineFriends)
            print("offfffffffffff",strListOfOfflineFriends)
            onlineFriends_msg = '{"msgType":"onlineFriendsMsg","onlineList":"'+strListOfOnlineFriends+'"}'
            offlineFriends_msg = '{"msgType":"offlineFriendsMsg","offlineList":"'+strListOfOfflineFriends+'"}'
            msgON = json.loads(onlineFriends_msg)
            dumpMessageON=json.dumps(msgON)
            msgOFF = json.loads(offlineFriends_msg)
            dumpMessageOFF=json.dumps(msgOFF)
            for c in clients:
                c['id'].write_message(dumpMessageON)
                c['id'].write_message(dumpMessageOFF)
            print(c['name'],"Send update to",c['currentRoom'])
            #////////////////////////////////// get Old Msgs from DB///////////////////////////////////////////////////
            msgObj=db.groupMsg.find({"GroupName":currentChatRoom},{"_id":0,"Msg":1})
            userObj=db.groupMsg.find({"GroupName":currentChatRoom},{"_id":0,"loginName":1})
            #global mes
            #global sender
            sender.clear()
            mes.clear()


            for val in userObj:
                sender.append(val['loginName'])

            for val in msgObj:
                mes.append(val['Msg'])


            if(roomType=='private'):
                print("some one entered Private room")

            if(roomType=='group'):
                strListOfDBmsg='>>'.join(mes)
                strListOfDBsender='>>'.join(sender)
                ListOfDBdata_msg = '{"msgType":"loadMsgs","DBsenders":"'+strListOfDBsender+'","DBmsgs":"'+strListOfDBmsg+'"}'
                DBmsg = json.loads(ListOfDBdata_msg)
                dumpDBmsg=json.dumps(DBmsg)

                for c in clients:
                    print(c['currentRoom'] ,">>>>>>>>>>>>>>", currentChatRoom)
                    if c['id']==self:
                        c['id'].write_message(dumpDBmsg)
                        print("Send DB old msgs to",c['name'])
        #//*************************************************************************************//
        #//************************************* Message ******************************************//
        if(msgType=='Message'):
            print("Type of msg->  Message")
            print("message-> ",msgContent,"from client->",senderName,"  TO-> ",currentChatRoom,roomType)

            ############# Save message in database ya Zaynb :D

            if(roomType=='private'):
                print("private connecion-------->",onlineFriends,"sender",sender,"msg",msg)
                for c in clients:
                    if (c['name']==currentChatRoom and c['currentRoom']==senderName) or c['id']==self:
                        c['id'].write_message(dumpMessage)
                        print(c['name'],"Send private Message to",c['currentRoom'])

            if(roomType=='group'):
                db.groupMsg.insert({"GroupName":currentChatRoom,"loginName":senderName,"Msg":msgContent})
                print("Group connecion -------->",onlineFriends)
                for c in clients:
                    print(c['currentRoom'] ,">>>>>>>>>>>>>>", currentChatRoom)
                    if c['currentRoom']==currentChatRoom:
                        c['id'].write_message(dumpMessage)
                        print(c['name'],"Send Group Message to",c['currentRoom'])


    def on_close(self):
        for c in clients:
            if c['id']==self:
                removedClient = c['name']
                clients.remove(c)
                onlineFriends.remove(c['name'])
                offlineFriends.append(c['name'])

        print("connection closed from: ",removedClient,"  NO.onlineFriends-> ", onlineFriends)





class chatPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../templates/chat.html")
