import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from pymongo import MongoClient
from bson.objectid import ObjectId

class LeaveGroupHandler(tornado.web.RequestHandler):
  def get(self):
     client = MongoClient('localhost', 27018)
     db = client.chatRR  # name of database
     collection=db['users'] # name of collection
     groupCollection=db['groups']
     usersCollection=db['allusers']
     # print("selfffffffff",self.data)
     name=self.get_query_arguments('Owner')
     group=self.get_query_arguments('Group')
     groupID=db.groups.find_one({"name":group[0]},{"_id":1})
     print("heeeeeeeee",groupID['_id']);
     userID=db.users.find_one({"name":name[0]},{"_id":1})
     x=userID['_id'];
     y=groupID['_id'];
     userObject=ObjectId(x);
     groupObject=ObjectId(y);
     db.groups.update(
                            {"name":group[0]},
                            {"$pull":{"members":userObject}}
                         )

     db.users.update(
                       {"name":name[0]},
                       {"$pull":{"groups":groupObject}}
                    )
