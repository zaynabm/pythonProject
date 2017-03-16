import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from pymongo import MongoClient
from bson.objectid import ObjectId


class CreateGroupHandler(tornado.web.RequestHandler):
  def get(self):
     client = MongoClient('localhost', 27018)
     db = client.chatRR  # name of database
     collection=db['users'] # name of collection
     groupCollection=db['groups']
     usersCollection=db['allusers']
     # print("selfffffffff",self.data)
     name=self.get_query_arguments('Owner')
     group=self.get_query_arguments('Group')
     path=self.get_query_arguments('path')
     print("grouuup",group);
     print("nnaaame",name);
    #  groupID=db.groups.find_one({"name":group[0]},{"_id":1})
     userID=db.users.find_one({"name":name[0]},{"_id":1})
    #  print("grouuuuuuupCreate",groupID['_id']);
     x=userID['_id'];
     userObj=ObjectId(x)
     print("userObj",userObj);
     print("x",x);
    #  userID=db.users.find_one({"_id":userObj},{"_id":1})
    #  print("userID",userID);
     print("paaath",path[0]);

    #--------------------------------------#
    #userID=db.userss.find_one({"name":owner},{"_id":1})
    # userVal=userID['_id']
    # userObj=ObjectId(userVal)
     addGroup = db.groups.insert_one(
      {

            "name": group[0],
            "owner":name[0],
            "members":[userObj],
            "img":path[0]
            # "description":desc
       }
     )
