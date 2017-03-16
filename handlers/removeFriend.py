import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from pymongo import MongoClient
from bson.objectid import ObjectId
from handlers.index import IndexHandler
import json


class RemoveFriendHandler(tornado.web.RequestHandler):
  def get(self):
     client = MongoClient('localhost', 27018)
     db = client.chatRR  # name of database
     collection=db['users'] # name of collection
     groupCollection=db['groups']
     usersCollection=db['allusers']
     # print("selfffffffff",self.data)
     name=self.get_query_arguments('Owner')
     friend=self.get_query_arguments('NameFriend')
     userID=db.users.find_one({"name":name[0]},{"_id":1})
     # print("heeeeeeeee",userID);
     friendID=db.users.find_one({"name":friend[0]},{"_id":1})
     x=userID['_id'];
     y=friendID['_id'];
     userObject=ObjectId(x);
     friendObject=ObjectId(y);
     db.users.update(
                            {"name":name[0]},
                            {"$pull":{"friends":friendObject}}
                         )
     db.users.update(
                       {"name":friend[0]},
                       {"$pull":{"friends":userObject}}
                    )
     emailObj=db.users.find_one({"name":name[0]},{"email":1,"_id":0})
     print(emailObj)
     email=emailObj['email']
     x= IndexHandler.allusersFun(self,email,db)
     print("xxxxxxxxx",x);
     #y=json.dumps(x)

     return "heeeeeee"
