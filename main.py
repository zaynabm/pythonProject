import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from pymongo import MongoClient

# ////////////////////////////////////////////////////////////////////////////////
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ("connecrion started")

    def on_message(self, message):
        self.write_message("Your message that recived was : " + message)

    def on_close(self):
        print("connection closed")

# ////////////////////////////////////////////////////////////////////////////////
class chatPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")

#--------------------------------------
#-----------------------------------------------------------------------------------
class MainPageHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/MainPage.html")
    def post(self):
          pass

class IndexHandler(tornado.web.RequestHandler):
      def post(self):
          print("hiiiiiiiii")
          self.render("templates/index.html")
          print("hellooooo")
          client = MongoClient('localhost', 27018)

          db = client.chatRR
          collection=db['users']
          groupCollection=db['groups']
          usersCollection=db['allusers']
          # result = db.createCollection("users")
          name= self.get_argument("name", "")
          if (name==""):
              print("oooooooooo")
              email=self.get_argument("email", "")
              password=self.get_argument("password", "")
              # name="aya"
              flag="false"
              userID=db.users.find_one({"email":email},{"_id":1})# 1 for true to get id only

              print(userID)
              if not(userID is None):
                  #print("hi")
                  flag="true"
                  for key, val in userID.items():

                     userPassword=db.users.find_one({"_id":val},{"password":1,"_id":0})# 1 for true to get pwd only

              givenPass=password
              if (flag is "true"):
                 for key, val in userPassword.items():
                    #print("ho")
                    print("val",val)
                    print("given",givenPass)
                    if(givenPass == val):
                       print("Right User")

                    else:
                       print("No Login")
                    #    self.render("test.html")

          else:
              print("naaaaaaaaaaaame",name)
              email=self.get_argument("email", "")
              age=self.get_argument("age", "")
              password=self.get_argument("password", "")
              #-------------add user (sign up)----------------

              userObj=db.users.find_one({"name":name},{"_id":1})
              print(userObj)
              if (userObj is None):

                  addUser = db.users.insert_one(
                  {

                          "name": name,
                          "password":password,
                          "age": age,
                          "email":email,

                  }
                  )
                  allUsers = db.allusers.insert_one(
                  {
                     "_id":id,
                  }
                  )
              else:
                  print("User already exists")


# ////////////////////////////////////////////////////////////////////////////////
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', chatPageHandler),
            (r'/ws', WebSocketHandler),
            (r"/MainPage", MainPageHandler),
            (r"/index", IndexHandler)
        ]
        tornado.web.Application.__init__(self, handlers, static_path='static',debug=True)


if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


