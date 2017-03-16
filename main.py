import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from pymongo import MongoClient
from handlers.chat import WebSocketHandler,chatPageHandler
from handlers.index import IndexHandler
from handlers.AddFriend import AddFriendHandler
from handlers.removeFriend import RemoveFriendHandler
from handlers.leaveGroup import LeaveGroupHandler
from handlers.joinGroup import JoinGroupHandler
from handlers.createGroup import CreateGroupHandler
# ////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------
class MainPageHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/MainPage.html",test="")

    def post(self):
          pass

# ////////////////////////////////////////////////////////////////////////////////
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/chat', chatPageHandler),
            (r'/ws', WebSocketHandler),
            (r"/MainPage", MainPageHandler),
            (r"/index", IndexHandler),
            (r"/addfriend",AddFriendHandler),
            (r"/removefriend",RemoveFriendHandler),
            (r"/leavegroup",LeaveGroupHandler),
            (r"/joingroup",JoinGroupHandler),
            (r"/createGroup",CreateGroupHandler)
        ]

        tornado.web.Application.__init__(self, handlers, static_path='static',debug=True)


if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
