import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from pymongo import MongoClient
from bson.objectid import ObjectId
from handlers.index import IndexHandler


class AddFriendHandler(tornado.web.RequestHandler):
       def get(self):
            client = MongoClient('localhost', 27018)
            print("wwwwwwwwwwwwwwwwwwwwwwww")
            db = client.chatRR  # name of database
            collection=db['users'] # name of collection
            groupCollection=db['groups']
            usersCollection=db['allusers']
            # print("selfffffffff",self.data)
            print("helooooooooooooo")
            name=self.get_query_arguments('Owner')
            friend=self.get_query_arguments('NameFriend')
            userID=db.users.find_one({"name":name[0]},{"_id":1})
            print("heeeeeeeee",userID);
            friendID=db.users.find_one({"name":friend[0]},{"_id":1})
            x=userID['_id'];
            y=friendID['_id'];
            userObject=ObjectId(x);
            friendObject=ObjectId(y);
            db.users.update(
                                   {"name":name[0]},
                                   {"$push":{"friends":friendObject}}
                                )

            db.users.update(
                              {"name":friend[0]},
                              {"$push":{"friends":userObject}}
                           )
            self.render("../templates/index.html");
            # return "gfgfgfg"
